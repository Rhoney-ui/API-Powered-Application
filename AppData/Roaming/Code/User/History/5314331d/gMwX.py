# DICTIONARIES: LABELLED DATA STORAGE

# Creating a dictionary

daily_log = {"steps": 9200, "water_glasses": 8, "cold_shower": True, "fasting_protocol": "OMAD", "sleep_hours": 7.5}

print (daily_log)

# Accessing Values

daily_log = {"steps": 9200, "water_glasses": 8, "cold_shower": True, "fasting_protocol": "OMAD", "sleep_hours": 7.5}

print ("Steps today:", daily_log ["steps"])
print ("Protocol:", daily_log ["fasting_protocol"])
print ("Cold shower:", daily_log ["cold_shower"])

# Adding & Updating Values

daily_log = {"steps": 9200, "water_glasses": 8, "fasting_protocol": "OMAD"}

# Add a new key
daily_log ["pages_read"] = 30
print ("After adding pages_read:", daily_log)

# Update an existing key
daily_log ["steps"] = 10400
print ("After updating steps:", daily_log)

# Deleting a Key

daily_log = {"steps": 9200, "water_glasses": 8, "fasting_protocol": "OMAD", "junk_entry": "delete me"}

del daily_log ["junk_entry"]
print (daily_log)

# Checking If a Key Exists

daily_log = {"steps": 9200, "water_glasses": 8, "fasting_protocol": "OMAD"}

if "steps" in daily_log:
    print ("Steps recorded:", daily_log ["steps"])

if "sleep_hours" not in daily_log:
    print ("Sleep hours not logged yet.")

# Looping Through a Dictionary

daily_log = {"steps": 9200, "water_glasses": 8, "cold_shower": True, "fasting_protocol": "OMAD", "sleep_hours": 7.5}

# Loop through keys and values together
for key, value in daily_log.items ():
    print (key,":", value)

# A Practical Dictionary

client = {"name": "James", "weight_kg": 84.5, "goal": "fat loss", "fasting_protocol": "2MAD", "bench_press_kg": 80, "weekly_sessions": 4}
print ("Client profile:")
for key, value in client.items ():
    print (f" {key}: {value}")

print ()

if client ["bench_press_kg"] >= 80:
    print ("Bench press goal reached.")

# EXERCISE

my_log = {"steps": 9400, "water_glasses": 7, "fasting_protocol": "OMAD", "cold_shower": True, "sleep_hours": 7.0}

for key, value in my_log.items ():
    print (key, ":", value)

print ()

if my_log ["steps"] >= 8000:
    print ("Step goal hit.")
else:
    print ("Step goal missed.")