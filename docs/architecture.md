# KrishiSaathi Architecture

## Current milestone

The repository starts as a modular Python backend. The architecture deliberately separates:

1. **Transport** — WebRTC/LiveKit or Pipecat.
2. **Speech** — Sarvam Saaras realtime STT.
3. **Reasoning** — Sarvam-105B conversational model.
4. **Tools** — verified weather, mandi and agricultural data providers.
5. **Speech output** — Sarvam Bulbul.
6. **Application state** — farmer, farm and conversation context.

## Data flow

```text
Farmer
  -> WebRTC transport
  -> Saaras realtime STT
  -> Agent Orchestrator
  -> Sarvam-105B
  -> Tool Router
  -> verified data providers
  -> Sarvam-105B
  -> Bulbul TTS
  -> Farmer
```

The first implementation milestone exposes a text turn boundary so the reasoning and tool layers can be tested independently of realtime audio.

## Engineering rules

- Live facts must come from tools, never from model invention.
- Deterministic calculations stay in Python.
- LLM output is kept concise for spoken responses.
- API keys stay server-side.
- Provider integrations are isolated behind adapters.
- Realtime transport must be replaceable without changing domain logic.
