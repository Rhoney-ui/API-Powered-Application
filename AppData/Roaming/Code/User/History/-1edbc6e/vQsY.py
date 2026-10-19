# WEEK 5 ASSIGNMENTS

# EXERCISE 1: HTTP REQUESTS

print("=== EXERCISE 1: HTTP REQUESTS ===")
import urllib.request, json

# Fetch a public API and print the response
url = "https://httpbin.org/json"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

print(json.dumps(data, indent=2))

# EXERCISE 2: PARSING JSON

print()
print("=== EXERCISE 2: PARSING JSON ===")
print()

import json
# parse this nested JSON and print the author and title
response = '{"book": {"title": "Clean Code", "author": "Robert Martin", "year": 2008}}'
data = json.loads(response)
book = data["book"]
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")