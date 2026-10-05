import pytest

from app.tools.mandi import get_mandi_price
from app.tools.weather import get_weather


@pytest.mark.asyncio
async def test_weather_provider_is_explicitly_unconfigured() -> None:
    with pytest.raises(NotImplementedError):
        await get_weather(
            location="Mandya",
            forecast_date=__import__("datetime").date.today(),
        )


@pytest.mark.asyncio
async def test_mandi_provider_is_explicitly_unconfigured() -> None:
    with pytest.raises(NotImplementedError):
        await get_mandi_price(
            commodity="tomato",
            market="Mandya",
            price_date=__import__("datetime").date.today(),
        )
