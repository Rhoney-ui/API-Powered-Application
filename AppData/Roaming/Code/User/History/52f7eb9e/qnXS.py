import requests

url = "https://restcountries.com"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print("Request failed. Status:, {response.status_code}")