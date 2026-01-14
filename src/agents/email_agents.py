from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from langchain_openai import ChatOpenAI


class EmailAssistantAgents:
    def __init__(self, llm: Any):
        self.llm = llm

    def summarise(self, email_text: str, context: str) -> str:
        prompt = f"""
        Summarise the following email clearly and concisely.

        Context:
        {context}

        Email:
        {email_text}
        """
        return self.llm.invoke(prompt).content

    @staticmethod
    def build_default() -> "EmailAssistantAgents":
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )
        return EmailAssistantAgents(llm=llm)
