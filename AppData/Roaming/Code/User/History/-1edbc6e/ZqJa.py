# WEEK 5 ASSIGNMENTS

# EXERCISE 1: HTTP REQUESTS



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