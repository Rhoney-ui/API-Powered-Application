import requests

def get_nairobi_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": -1.2921,
        "longitude": 36.8219,
        "current": (
            "temperature_2m,relative_humidity_2m,apparent_temperature,"
            "precipitation,weather_code,wind_speed_10m,wind_direction_10m"
        ),
        "timezone": "Africa/Nairobi",
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json().get("current", {})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def describe_weather_code(code):
    codes = {
        0: "Clear sky",
        1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Fog", 48: "Depositing rime fog",
        51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
        56: "Light freezing drizzle", 57: "Dense freezing drizzle",
        61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
        66: "Light freezing rain", 67: "Heavy freezing rain",
        71: "Slight snow fall", 73: "Moderate snow fall", 75: "Heavy snow fall",
        77: "Snow grains",
        80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
        85: "Slight snow showers", 86: "Heavy snow showers",
        95: "Thunderstorm", 96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail",
    }
    return codes.get(code, "Unknown weather condition")


def compass_direction(degrees):
    """Convert wind degrees to a compass direction like NNE, SW, etc."""
    if degrees is None:
        return "N/A"
    directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                  "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    index = int((degrees + 11.25) // 22.5) % 16
    return directions[index]


def print_weather_summary(current):
    if not current:
        print("No weather data available.")
        return

    wind_dir = current.get("wind_direction_10m")
    wind_dir_str = f"{compass_direction(wind_dir)} ({wind_dir}°)"

    print("=" * 42)
    print("     CURRENT WEATHER IN NAIROBI")
    print("=" * 42)
    print(f"Time:          {current.get('time', 'N/A')}")
    print(f"Condition:     {describe_weather_code(current.get('weather_code'))}")
    print(f"Temperature:   {current.get('temperature_2m', 'N/A')} °C")
    print(f"Feels like:    {current.get('apparent_temperature', 'N/A')} °C")
    print(f"Humidity:      {current.get('relative_humidity_2m', 'N/A')} %")
    print(f"Precipitation: {current.get('precipitation', 'N/A')} mm")
    print(f"Wind:          {current.get('wind_speed_10m', 'N/A')} km/h {wind_dir_str}")
    print("=" * 42)


if __name__ == "__main__":
    print_weather_summary(get_nairobi_weather())