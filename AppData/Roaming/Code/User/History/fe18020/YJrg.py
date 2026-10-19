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
    # Check if steps meet the goal
    status = "Goal met" if data["steps"] >= 10000 else "Short"
    print(f"Fetched: {data['name']} ({data['steps']} steps) {status}")
    # In production: time.sleep(0.5) to avoid rate limits

print(f"\nTotal fetched: {len(results)}")

# A Kenyan business Example: M-Pesa Daraja API
# SIMULATE M-PESA DARAJA AUTH FLOW

import os
import base64

# Step 1: Load credentials from environment (never hardcore)
os.environ["MPESA_CONSUMER_KEY"] = "demo_consumer_key_abc123"
os.environ["MPESA_CONSUMER_SECRET"] = "demo_secret_xyz789"

consumer_key = os.getenv("MPESA_CONSUMER_KEY")
consumer_secret = os.getenv("MPESA_CONSUMER_SECRET")

# Step 2: Encode credentials (Daraja requires Base64)
credentials = f"{consumer_key}: {consumer_secret}"
encoded = base64.b64encode(credentials.encode()).decode()

# Step 3: In production you POST this to Daraja to get a token:
# url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
# headers = {"Authorization": f"Basic {encoded}"}
# response = requests.get(url, heders=headers)
# token = response.json() ["access_token"]

# Simulate the token response
simulated_token = "Q2xpZW50X01ENmJ1YjA2NWEtMjA4Ny000TU2"

print()
print("=== SIMULATE M-PESA DARAJA AUTH FLOW ===")
print()
print("Credentials encoded(Base64):", encoded[:20] + "...")
print()
print("Simulated token received:", simulated_token[:20] + "...")
print()
print("In production, pass this token to every M-Pesa API call:")
print(f' headers = {{"Authorization": "Bearer {simulated_token[:12]}..."}}')
print()
print("Example endpoint: STK Pust (prompt customer to pay)")
print(" POST https:..sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest")

# What This Looks Like with a Real API: Facebook Graph
# PARSE A FACEBOOK GRAPH API RESPONSE

import os

# Step 1: Load the token from environment (never hardcore it)
os.environ["FB_ACCESS_TOKEN"] = "EAADemo_token_never_hardcore_real_ones"
token = os.getenv("FB_ACCESS_TOKEN")

# Step 2: This is what the Graph API returns for facebook.com/amerix041
fb_response = {
    "id": "100044385041",
    "name": "Amerix",
    "about": "reproductive Health | Men's health and Wellness",
    "fan_count": 284000,
    "followers_count": 291500,
    "category": "Health & Wellness Website",
    "link": "https://www.facebook.com/amerix041"
}

# Step 3: Parse it exactly as you have learned
name = fb_response["name"]
about = fb_response["about"]
fans = fb_response["fan_count"]
followers = fb_response["followers_count"]
page_link = fb_response["link"]

print()
print("FACEBOOK PAGE DATA")
print()
print(f" Page: {name}")
print(f" About: {about}")
print(f" Page likes: {fans:,}")
print(f" Followers: {followers:,}")
print(f" Link: {page_link}")
print()
print(f" Token loaded: {token[:12]}... (never log a live token)")
print()
print("Note: in production, replace the mock response with:")
print(" response = requests.get(url, params={'access_token': token,'fields': '...'})")
print(" data = response.json()")