# Building a Live Data Script 
# The Four-Part Structure - Configuration, Fetch, Process, Output

# PART 1: Configuration
# CONFIGURATION BLOCK

import os

# Configuration
BASE_URL = "https://api.smptracker.com/v1"
API_KEY = os.environ.get("SMP_API_KEY", "demo_key_123")
DEFAULT_CITY = "Nairobi"
STEP_GOAL = 10000
MAX_RESULTS = 50

print()
print("=== CONFIGURATION BLOCK ===")
print()

print("Configuration loaded:")
print(f" Base URL: {BASE_URL}")
print(f" API key: {API_KEY[:8]}...")
print(f" City: {DEFAULT_CITY}")
print(f" Step Goal: {STEP_GOAL:,}")
print(f" Max Results: {MAX_RESULTS}")

# PART 2: Fetch Function
# FETCH FUNCTION PATTERN

# Simulate what a fetch function does in a script

print()
print("=== FETCH FUNCTION PATTERN ===")
print()
def fetch_members(city="Nairobi", limit=50):
    """
    Fetches member data from the SMP API.
    Returns a list of member dicts or raises RuntimeError.
    In production: uses requests.get() with headers and params.
    """
    # Simulate the API response
    mock_response_status = 200
    mock_data = [
        {"id": 1, "name": "James Omondi", "city": "Nairobi", "steps": 9200, "protocol": "OMAD"},
        {"id": 2, "name": "Sandra weru", "city": "Nairobi", "steps": 10500, "protocol": "2MAD"},
        {"id": 3, "name": "Patrick Njiru", "city": "Mombasa", "steps": 8100, "protocol": "OMAD"},
        {"id": 4, "name": "Grace Achieng", "city": "Nairobi", "steps": 11000, "protocol": "OMAD"},
        {"id": 5, "name": "Brian Kamau", "city": "Kisumu", "steps": 7400, "protocol": "2MAD"},
        {"id": 6, "name": "Kevin Mwangi", "city": "Nairobi", "steps": 10800, "protocol": "OMAD"},
    ]

if mock_response_status == 200:
    raise RuntimeError(f"API error: status{mock_response_status}")

    # Filter by city
    filtered = [m for m in mock_data if m["city"] == city]
    return filtered[:limit]

# Call the function
members = fetch_members(city="Nairobi")
print(f"Fetched {len(members)} members from Nairobi")
for m in members:
    print(f" {m['name']}: {m['steps']} steps")
