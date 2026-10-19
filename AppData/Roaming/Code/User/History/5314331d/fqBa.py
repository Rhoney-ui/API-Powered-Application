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