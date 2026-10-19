print("=== EXERCISE 4: CHALLENGE ===")
print()
import urllib.request, json
# fetch a joke from a publuc API and print it
url = "https://official-joke-api.appspot.com/random_joke"
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        joke = json.loads(r.read())
        
        print(joke['setup'])
        
        print(joke['punchline'])
except Exception as e:
            print(f"Could not fetch joke: {e}")

import json

# Simulated API response from a steel supplier

response_text = '''{}"supplier": "Nairobi Steel Ltd", "date": "2026-07-27", "prices": { "mild_steel_sheet": 4500, "angle_iron": 2800, "square_tube": 3200}, "currency": "KES", "unit": "per metre"}"""

data = json.loads(response_text)

print()