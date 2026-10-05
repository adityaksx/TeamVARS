from app.agent.orchestrator import AgentOrchestrator
from app.voice.models import VoiceResponse, VoiceTurn


class VoiceService:
    """Application-level voice turn service.

    Realtime WebRTC transport will feed finalized STT turns into this service.
    Keeping the transport separate lets us test agent behavior without audio.
    """

    def __init__(self, orchestrator: AgentOrchestrator) -> None:
        self.orchestrator = orchestrator

    async def handle_turn(self, turn: VoiceTurn) -> VoiceResponse:
        result = self.orchestrator.respond(turn.transcript)

        # The Sarvam SDK response shape is normalized here later when the
        # streaming voice pipeline is connected.
        text = getattr(
            getattr(result, "choices", [None])[0],
            "message",
            None,
        )
        content = getattr(text, "content", None) or str(result)

        return VoiceResponse(
            session_id=turn.session_id,
            text=content,
            language_code=turn.language_code,
        )
