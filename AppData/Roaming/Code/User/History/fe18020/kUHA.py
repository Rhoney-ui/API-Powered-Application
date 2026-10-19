# pip in Practice: Installing Packages for Your Projects

# API Keys and Authentication
# Why APIs Require Authentication
# The Key Safety Rule - Never put an API key directly in your code.

# METHOD 1: Environment Variables
# SIMULATE READING AN ENV VARIABLE

print()
print("=== METHOD 1: ENVIRONMENT VARIABLE (SIMULATE READING AN ENV VARIABLE) ===")
print()
import os

# Simulate: key loaded from environment (not hardcoded)
os.environ["SMP_API_KEY"] = "smp_test_key_abc123" # set for demo only

api_key = os.environ.get("SMP_API_KEY")

if not api_key: 
    print("ERROR: API key not found. Set the SMP_API_KEY environment variable.")
else: 
    # Show only first 8 chars for safety
    masked = api_key[:8] + "..." + api_key[-4:]
    print(f"Key loaded: {masked}")
    print("Ready to make authenticated requests.")

# METHOD 2: The .env File (Recommended)
# Passing Keys in Requests
# METHOD A - Query Parameter in the URL
# METHOD B - Authorization Header

# SIMULATE AUTHENTICATED REQUEST STRUCTURE

print()
print("=== METHOD 2 - .env File (AUTHENTICATED REQUEST STRUCTURE SIMULATION) ===")
print()
import os

# simulate: load key from environment
os.environ["SMP_API_KEY"] = "smp_live_abc123xyz"
api_key = os.getenv("SMP_API_KEY")

# Build request components (what you would pass to requests.get)
url = "https://api.smptracker.com/v1/members"
params = {"city": "Nairobi", "limit": 10}
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

print("URL:", url)
print("Params:", params)
print("Auth header:", "Bearer" + api_key[:8] + "...")

# Simulate a 200 response
print()
print("Response status: 200")
print("Response body: {'members': [...], 'total': 42}")

# Handling Authentication Errors
# HANDLE AUTH ERRORS

print()
print("=== HANDLING AUTHENTICATION ERRORS ===")
print()
def handle_api_response(status_code, body):
    if status_code == 200:
        return body
    elif status_code == 401:
        raise PermissionError("Authentication failed. Check your API key.")
    elif status_code == 403:
        raise PermissionError("Access denied. Your key does not have permission for this endpoint.")
    elif status_code == 429:
        raise RuntimeError("Rate limit exceeded. Wait before retrying.")
    elif status_code >= 500:
        raise RuntimeError(f"Server error ({status_code}). try again later.")
    else:
        raise RuntimeError(f"Unexpected status: {status_code}")

# Test with different status codes
test_cases = [
    (200, {"members": [{"name": "James Omondi"}]}),
    (401, {"error": "invalid_key"}),
    (429, {"error": "rate_limit_exceeded"}),
    (500, {"error": "internal_server_error"}),
]

for status, body in test_cases:
    try: 
        result = handle_api_response(status, body)
        print(f"Status {status}: OK, got {result}")
    except Exception as e:
        print(f"Status {status}: {e}")

# Rate Limits 
# RATE LIMIT SIMULATION

# Simulate making multiple API calls with a delay
member_ids = [1, 2, 3, 4, 5]

print()
print("=== RATE LIMIT SIMULATION ===")
print()

def fetch_member(member_id):
    # Simulates what requests.get would return
    steps_goal = 10000
    mock_data = {
        1: {"name": "James Omondi", "steps": 9200},
        2: {"name": "Sandra Weru", "steps": 10500},
        3: {"name": "Patrick Njiru", "steps": 8100},
        4: {"name": "Grace Achieng", "steps": 11000},
        5: {"name": "Brian Kamau", "steps": 7400},
    }
    return mock_data.get(member_id)

results = []
for mid in member_ids:
    data = fetch_member(mid)
    results.append(data)
    print(f"Fetched: {data['name']} ({data['steps']} steps)")
    # In production: time.sleep(0.5) to avoid rate limits

# Check if steps meet the goal
status = "Goal met" if data["steps"] >= 10000 else "Short"
print(f"{data['name']} {data['steps']} steps {status}")
print(f"\nTotal fetched: {len(results)}")