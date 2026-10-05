# KrishiSaathi AI

A multilingual, voice-first agricultural decision assistant built for Sarvam AI's Applied AI problem statement.

## Current architecture

- FastAPI backend
- Sarvam SDK integration boundary
- Agent/tool orchestration
- Weather and mandi tool interfaces
- Farmer context models
- Retry/resiliency utilities
- React frontend scaffold planned for the next milestone

## Development

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

The first milestone intentionally establishes clean interfaces before wiring live voice transport. Sarvam API keys must remain server-side and must never be committed.

## Roadmap

1. Sarvam client + health checks
2. Weather and mandi tools
3. Sarvam tool-calling agent
4. Realtime Saaras voice pipeline
5. Bulbul streaming TTS
6. WebRTC transport
7. Farmer profile and personalization
8. Barge-in, telemetry and production hardening
