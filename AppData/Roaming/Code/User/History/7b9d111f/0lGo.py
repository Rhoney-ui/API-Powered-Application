# Working with JSON
# json.dumps(): Python to JSON Text

import json

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}

# Concert to JSON string 
json_text = json.dumps(daily_log)
print("Type:", 
type(json_text))
print("JSON:", json_text)

# Pretty print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nPretty JSON:")
print(pretty)

# json.loads(): JSON Text to Python

import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true,"protocol": "OMAD"}'

# Convert JSON string to Python dictionary
data = json.loads(api_response)

print()
print("--- JSON TEXT TO PYTHON ---")
print()
print("Type:", type(data))
print("Steps:", data["steps"])
print("Cold shower:", data["cold_shower"])
print("Protocol:", data["protocol"])