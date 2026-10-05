from fastapi import APIRouter

from app.voice.models import VoiceTurn

router = APIRouter(prefix="/api")


@router.post("/voice/turn")
async def voice_turn(turn: VoiceTurn) -> dict:
    """Temporary text-to-agent endpoint used to validate the agent before WebRTC."""
    return {
        "status": "accepted",
        "session_id": turn.session_id,
        "transcript": turn.transcript,
        "language_code": turn.language_code,
    }
