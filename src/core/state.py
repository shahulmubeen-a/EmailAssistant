from typing import Annotated, List, TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    """
    Represents the state of the email assistant graph.
    
    Attributes:
        messages: A list of messages in the conversation.
        email_content: The raw content of the email being processed.
        category: The categorised type of the email (e.g., 'Procurement', 'Safety', 'General').
        draft_reply: The generated draft for the email reply.
        context: Relevant information retrieved from the vector store.
    """
    messages: Annotated[List[dict], add_messages]
    email_content: str
    category: str
    draft_reply: str
    context: List[str]
