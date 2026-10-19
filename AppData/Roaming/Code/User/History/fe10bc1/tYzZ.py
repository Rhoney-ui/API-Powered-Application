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

# When a Value Could Be None
# HANDLE NONE VALUES

print()
print("=== HANDLE NONE VALUES ===")
print()
users = [
    {"name": "James Omondi", "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru", "workout": None},  # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:
        bench = workout.get("bench_press_kg", "not recorded")
        mins = workout.get("duration_minutes", "?")
        print(f"{name}: banch={bench}kg, duration={mins}min")
