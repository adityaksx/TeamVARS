from app.tools.mandi import get_mandi_price
from app.tools.weather import get_weather

TOOL_REGISTRY = {
    "get_weather": get_weather,
    "get_mandi_price": get_mandi_price,
}
