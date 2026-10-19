# WHAT IS AN API?
# HTTP Methods - GET, POST, PUT, DELETE
# Status Codes - 200, 201, 400, 401, 404, 500
# What the request Library Does - pip install requests

# Working with a Simulated Response

# Simulates what response.json() returns from a fitness API
data = {
    "user_id": 1,
    "name": "James Omondi",
    "date": "2024-11-18",
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD"
    "sleep_hours": 7.5,
    "workout_completed": True
}

print("Name:", data["name"])
print("Steps:", data["steps"])
print("Protocol:", data["fasting_protocol"])
print("Cold shower:", data["cold_shower"])
print("Sleep:", data["sleep_hours"], "hours")