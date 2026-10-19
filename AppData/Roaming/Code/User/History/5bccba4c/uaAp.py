import os

import requests

# --- Configuration ---
# Never hardcode keys; read them from environment variables (or a .env file)
API_KEY = os.getenv("RESTCOUNTRIES_API_KEY")
BASE_URL = "https://api.restcountries.com/countries/v5/name"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}

def get_country_info(country_name: str) -> None:
    """Fetch and print basic info about a country."""

    if not API_KEY:
        print("[ERROR] Environment variable RESTCOUNTRIES_API_KEY is not set.")
        print("        Please create an API key at https://restcountries.com first.")
        return

    url = f"{BASE_URL}/{country_name}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network problem: {e}")
        return

    # Handle non-200 responses
    if response.status_code != 200:
        print(f"[FAILED] Status code: {response.status_code}")
        print(f"[DETAIL] {response.text}")
        return

    # Safely parse JSON
    try:
        data = response.json()
    except ValueError:
        print("[ERROR] Response was not valid JSON.")
        return

    if not data:
        print(f"[WARN] No data returned for '{country_name}'.")
        return

    # v5 response structure may differ from v3.1
    # Check the actual returned fields first, then extract as needed
    print("\n" + "=" * 40)
    print(f"  Country    : {country_name.title()}")
    print(f"  Raw preview: {str(data)[:200]}...")
    print("=" * 40 + "\n")

if __name__ == "__main__":
    # Replace with any country you want to query
    get_country_info("kenya")