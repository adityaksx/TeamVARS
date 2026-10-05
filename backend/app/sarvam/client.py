from sarvamai import SarvamAI

from app.config.settings import get_settings


class SarvamClient:
    """Server-side gateway for all Sarvam API access."""

    def __init__(self) -> None:
        settings = get_settings()
        if not settings.sarvam_api_key:
            raise RuntimeError(
                "SARVAM_API_KEY is not configured. "
                "Set it in backend/.env for live API access."
            )
        self.client = SarvamAI(api_subscription_key=settings.sarvam_api_key)

    def chat(self, *, model: str, messages: list[dict]) -> object:
        return self.client.chat.completions(
            model=model,
            messages=messages,
        )
