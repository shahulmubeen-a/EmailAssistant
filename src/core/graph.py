from typing import Any


class EmailGraph:
    def __init__(self, agents: Any, rag: Any):
        self.agents = agents
        self.rag = rag

    def run(self, query: str) -> str:
        context = self.rag.retrieve(query)
        response = self.agents.generate(query, context)
        return response


def create_email_graph(agents, rag) -> EmailGraph:
    return EmailGraph(agents=agents, rag=rag)
