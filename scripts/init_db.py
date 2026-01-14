from langchain.docstore.document import Document
from src.core.rag import EmailRAG
import os
import sys

# Add src to path so we can import from it
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def initialise_database():
    # Sample construction domain data for RAG
    construction_docs = [
        Document(page_content="Procurement Policy: All steel orders above £50,000 require approval from the Project Manager and must be logged in the ERP system.", metadata={"source": "procurement_manual"}),
        Document(page_content="Safety Protocol: Site inspections are mandatory every Tuesday at 08:00. Any safety violations must be reported via the SiteSafe app within 2 hours.", metadata={"source": "safety_manual"}),
        Document(page_content="Planning Guidelines: Project delays exceeding 5 days require a formal 'Notice of Delay' to be sent to the client representative.", metadata={"source": "planning_manual"}),
        Document(page_content="Vendor List: Approved concrete suppliers for the London region include BuildRight Ltd and MetroMix Co.", metadata={"source": "vendor_list"}),
    ]

    print("Initialising FAISS index with construction domain context...")
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    rag = EmailRAG()
    rag.initialise_with_docs(construction_docs)
    
    print("Database initialised successfully at data/faiss_index")

if __name__ == "__main__":
    initialise_database()
