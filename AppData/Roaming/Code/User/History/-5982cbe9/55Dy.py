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