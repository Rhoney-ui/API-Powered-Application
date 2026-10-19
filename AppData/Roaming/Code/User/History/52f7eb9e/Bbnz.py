import requests

url = "https://api.restcountries.com/v3.1/name/kenya"
headers = {
    "Authorization": "Bearer YOUR_API_KEY_HERE" # Replace with your actual key
}

response = requests.get(url, headers=headers, timeout=10)

if response.status_code == 200:
    data = response.json()
    country = data[0]

    name = country["name"]["common"]
    capital = country.get("capital", ["N/A"])[0]
    population = country["population"]
    currency = country.get("currencies", {})
    currency_code = list(currencies.keys())[0] if currencies else "N/A"
    
    print(f"Country: {name}")
    print(f"Capital: {capital}")
    print(f"Population: {population:,}")
    print(f"Currency: {currency_code}")
else:
    print("Request failed. Status:", response.status_code)
    print("Response:", response.text)