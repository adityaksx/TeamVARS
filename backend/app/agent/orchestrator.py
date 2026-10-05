from app.agent.prompts import SYSTEM_PROMPT
from app.sarvam.client import SarvamClient


class AgentOrchestrator:
    """Coordinates Sarvam reasoning and future tool execution."""

    def __init__(self, client: SarvamClient) -> None:
        self.client = client

    def respond(self, user_message: str) -> object:
        return self.client.chat(
            model="sarvam-105b-conversations",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
        )
