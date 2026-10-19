# PARSING API RESPONSES

# Deeply Nested Responses

# NAVIGATE NESTED STRUCTURE

response = {
    "status": "success",
    "user": {
        "id": 42,
        "name": "Kevin Mwangi",
        "location": {
            "city": "Kisumu",
            "country": "Kenya"
        }
    },
    "today": {
        "steps": 10800,
        "cold_shower": True,
        "fasting": {
            "protocol": "OMAD",
            "window_hours": 23
        },
        "workout": {
            "completed": True,
            "bench_press_kg": 90,
            "duration_minutes": 55
        }
    }
}

# Navigate layer by layer
name = response["user"] ["name"]
city = response["user"] ["location"] ["city"]
steps = response["today"] ["steps"]
protocol = response["today"] ["fasting"] ["protocol"]
bench = response["today"] ["workout"] ["bench_press_kg"]

print()
print("=== NAVIGATE NESTED STRUCTURE ===")
print()
print(f"Name:  {name}")
print(f"City:  {city}")
print(f"Steps:  {steps}")
print(f"Protocol:  {protocol}")
print(f"Bench:  {bench} kg")