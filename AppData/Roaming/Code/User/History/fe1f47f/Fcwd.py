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
