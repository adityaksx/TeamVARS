from datetime import date
from pydantic import BaseModel


class MandiPriceResult(BaseModel):
    commodity: str
    market: str
    price: float
    unit: str
    price_date: date
    source: str


async def get_mandi_price(
    *,
    commodity: str,
    market: str,
    price_date: date,
) -> MandiPriceResult:
    """Mandi provider adapter placeholder.

    Live prices must come from a verified source; the LLM is never allowed
    to invent a market price.
    """
    raise NotImplementedError(
        "Connect a verified mandi-price provider before enabling this tool."
    )
