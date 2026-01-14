from langgraph.graph import StateGraph, END
from src.core.state import AgentState
from src.agents.email_agents import EmailAssistantAgents

def create_email_graph():
    agents = EmailAssistantAgents()
    workflow = StateGraph(AgentState)

    # Define nodes
    workflow.add_node("categorise", agents.categorise_email)
    workflow.add_node("retrieve", agents.retrieve_context)
    workflow.add_node("draft", agents.draft_reply)

    # Define edges
    workflow.set_entry_point("categorise")
    workflow.add_edge("categorise", "retrieve")
    workflow.add_edge("retrieve", "draft")
    workflow.add_edge("draft", END)

    return workflow.compile()
