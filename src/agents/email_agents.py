from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.core.state import AgentState
from src.core.rag import EmailRAG

class EmailAssistantAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.rag = EmailRAG()

    def categorise_email(self, state: AgentState):
        """
        Categorises the incoming email into specific construction-related categories.
        """
        email_content = state["email_content"]
        prompt = f"""
        You are an expert AI Assistant for a construction firm. 
        Categorise the following email into one of these categories:
        - Procurement: Related to buying materials, equipment, or services.
        - Safety: Related to site safety, inspections, or compliance.
        - Planning: Related to project schedules, delays, or milestones.
        - General: Any other business communication.

        Email Content: {email_content}
        
        Respond with ONLY the category name.
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return {"category": response.content.strip()}

    def retrieve_context(self, state: AgentState):
        """
        Retrieves relevant context based on the email content and category.
        """
        query = state["email_content"]
        context = self.rag.retrieve_context(query)
        return {"context": context}

    def draft_reply(self, state: AgentState):
        """
        Drafts a professional reply using the retrieved context and category.
        """
        email_content = state["email_content"]
        category = state["category"]
        context = "\n".join(state["context"])
        
        prompt = f"""
        You are an AI Assistant for a construction firm. 
        Draft a professional reply to the following email.
        
        Category: {category}
        Context from past records: {context}
        Original Email: {email_content}
        
        Ensure the tone is professional and addresses the specific points in the email.
        Use British English spelling (e.g., 'optimise', 'organisation', 'programme').
        """
        response = self.llm.invoke([HumanMessage(content=prompt)])
        return {"draft_reply": response.content.strip()}
