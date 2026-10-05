from pydantic import BaseModel, Field


class VoiceTurn(BaseModel):
    session_id: str
    transcript: str = Field(min_length=1)
    language_code: str | None = None


class VoiceResponse(BaseModel):
    session_id: str
    text: str
    language_code: str | None = None
