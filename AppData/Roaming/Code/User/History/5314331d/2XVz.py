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
for key, value in daily_log.values ():
    print (key,":", value)