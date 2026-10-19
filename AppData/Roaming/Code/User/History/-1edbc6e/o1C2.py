# WEEK 5 ASSIGNMENTS

# EXERCISE 1: HTTP REQUESTS

print("=== EXERCISE 1: HTTP REQUESTS ===")
import urllib.request, json

# Fetch a public API and print the response
url = "https://httpbin.org/json"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print(json.dumps(data, indent=2))

