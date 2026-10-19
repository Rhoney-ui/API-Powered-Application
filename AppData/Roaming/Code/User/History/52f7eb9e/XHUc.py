import requests

url = "https://restcountries.com"
headers = {"Authorization": "Bearer YOUR_API_KEY"} # Replace with your v5 API key

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Adjust parsing based on the v5 response structure
    print(data)
else:
    print(f"Request failed. Status: {response.status_code}")