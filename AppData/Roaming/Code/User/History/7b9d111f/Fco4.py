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

# WORKING WITH JSON FILES
# SIMULATE FILE READ AND WRITE

import json

print()
print("--- SIMULATE FILE READ AND WRITE ---")
print()
# Simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)

# Simulate reading it back
loaded_data = json.loads(json_string)
print("\nRead back as Python dict:")
for key, value in loaded_data.items():
    print(f" {key}: {value}")

# NAVIGATING NESTED JSON
# NESTED JSON

import json

# Simulated API response with nested data

print()
print("--- NAVIGATING NESTED JSON ---")
print()
api_json = '''
{
"client": "James Omondi",
"week": 1,
"daily_logs": [
{"day": "Monday", "steps": 9200, "protocol": "OMAD"},
{"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
{"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
{"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon"},
{"day": "Friday", "steps": 7600, "protocol": "OMAD"},
{"day": "Saturday", "steps": 10000, "protocol": "OMAD"}
]
}
'''

data = json.loads(api_json)

print("Client:",
data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f" {log['day']}: {log['steps']} steps ({status})")

# JSON AND ERROR HANDLING
import json

print()
print("--- JSON AND ERROR HANDLING ---")
responses = [
    '{"steps": 9200, "protocol": "OMAD"}', 'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")

# EXERCISE

import json

print()
print("--- EXERCISE (WEEK 4 - DAY 3) ---")
week_report = {
    "name": "James",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")
