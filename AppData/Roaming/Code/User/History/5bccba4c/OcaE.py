import requests

# --- Configuration ---
API_KEY = "YOUR_API_KEY_HERE"   # Get one at https://restcountries.com
COUNTRY = "kenya"
URL = f"https://restcountries.com/v3.1/name/{COUNTRY}"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}


def get_country_info(country_name: str) -> None:
    """Fetch and print basic info about a country."""

    try:
        response = requests.get(URL, headers=HEADERS, timeout=10) # always "kenya"
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network problem: {e}")
        return

    # --- Handle non-200 responses ---
    if response.status_code != 200:
        print(f"[FAILED] Status code: {response.status_code}")
        print(f"[DETAIL] {response.text}")
        return

    # --- Parse JSON safely ---
    data = response.json()

    if not data:
        print("[WARN] No data returned for that country.")
        return

    country = data[0]

    name       = country["name"]["common"]
    capital    = country.get("capital", ["N/A"])[0]
    population = country["population"]

    currencies     = country.get("currencies", {})
    currency_code  = list(currencies.keys())[0] if currencies else "N/A"
    currency_name  = currencies[currency_code]["name"] if currencies else "N/A"

    # --- Print results ---
    print("\n" + "=" * 40)
    print(f"  Country    : {name}")
    print(f"  Capital    : {capital}")
    print(f"  Population : {population:,}")
    print(f"  Currency   : {currency_name} ({currency_code})")
    print("=" * 40 + "\n")


if __name__ == "__main__":
    get_country_info(COUNTRY)