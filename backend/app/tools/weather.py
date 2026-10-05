from datetime import date
from pydantic import BaseModel


class WeatherResult(BaseModel):
    location: str
    forecast_date: date
    rainfall_probability: float
    rainfall_mm: float | None = None
    source: str


async def get_weather(
    *,
    location: str,
    forecast_date: date,
) -> WeatherResult:
    """Weather provider adapter placeholder.

    The provider is intentionally isolated here so the agent never fabricates
    current weather when an upstream data source is unavailable.
    """
    raise NotImplementedError(
        "Connect a verified weather provider before enabling this tool."
    )
