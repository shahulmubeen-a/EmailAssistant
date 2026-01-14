import os
from typing import List
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document

class EmailRAG:
    """
    Handles Retrieval-Augmented Generation using FAISS for email context.
    """
    def __init__(self, index_path: str = "data/faiss_index"):
        self.index_path = index_path
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = None
        
        if os.path.exists(index_path):
            self.vector_store = FAISS.load_local(index_path, self.embeddings, allow_dangerous_deserialization=True)

    def initialise_with_docs(self, documents: List[Document]):
        """
        Initialises the FAISS index with a list of documents.
        """
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        self.vector_store.save_local(self.index_path)

    def retrieve_context(self, query: str, k: int = 3) -> List[str]:
        """
        Retrieves relevant context for a given query.
        """
        if not self.vector_store:
            return ["No context available."]
        
        docs = self.vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
