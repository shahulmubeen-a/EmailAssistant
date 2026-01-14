from typing import TYPE_CHECKING, Any, List

if TYPE_CHECKING:
    from langchain_community.vectorstores import FAISS


class EmailRAG:
    def __init__(self, vector_store: Any):
        self.vector_store = vector_store

    def retrieve(self, query: str) -> str:
        docs = self.vector_store.similarity_search(query, k=3)
        return "\n".join(doc.page_content for doc in docs)

    @staticmethod
    def build_default(index_path: str) -> "EmailRAG":
        from langchain_community.vectorstores import FAISS

        vector_store = FAISS.load_local(
            index_path,
            allow_dangerous_deserialization=True,
        )
        return EmailRAG(vector_store)

    @staticmethod
    def build_from_documents(
        documents: List[Any], embeddings: Any
    ) -> "EmailRAG":
        from langchain_community.vectorstores import FAISS

        vector_store = FAISS.from_documents(documents, embeddings)
        return EmailRAG(vector_store)
