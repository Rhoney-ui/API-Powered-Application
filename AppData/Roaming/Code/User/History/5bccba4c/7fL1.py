import requests

# WMO Weather interpretation codes (partial, covering common conditions)
# Source: Open-Meteo documentation [citation:1][citation:14]
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    95: "Thunderstorm",
}

def get_weather_summary(city_name: str, latitude: float, longitude: float) -> None:
    """Fetches current weather from Open-Meteo and prints a clean summary."""

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,weather_code,wind_speed_10m,relative_humidity_2m",
        "timezone": "auto",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises an exception for 4xx/5xx status codes
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch weather data: {e}")
        return

    data = response.json()
    current = data.get("current", {})

    if not current:
        print("[WARN] No current weather data found in the response.")
        return

    # Extract and map values
    temperature = current.get("temperature_2m")
    feels_like = current.get("apparent_temperature")
    humidity = current.get("relative_humidity_2m")
    wind_speed = current.get("wind_speed_10m")
    weather_code = current.get("weather_code")
    condition = WEATHER_CODES.get(weather_code, "Unknown weather condition")

    # Print the human-readable summary
    print("\n" + "=" * 45)
    print(f"  Current Weather for {city_name.title()}")
    print("=" * 45)
    print(f"  Condition      : {condition}")
    print(f"  Temperature    : {temperature} °C")
    print(f"  Feels Like     : {feels_like} °C")
    print(f"  Humidity       : {humidity} %")
    print(f"  Wind Speed     : {wind_speed} km/h")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    # Example: London coordinates
    # You can change these to any city's latitude and longitude
    get_weather_summary("London", 51.5085, -0.1257)
