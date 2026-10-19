# NESTED DATA: LISTS INSIDE DICTIONARIES.

# A List of Dictionaries

week_log = [{"day": "Monday", "steps": 9200, "protocol": "OMAD", "cold_shower": True}, {"day": "Tuesday", "steps": 10500, "protocol": "2MAD", "cold_shower": True}, {"day": "Wednesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False}, {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon", "cold_shower": True}, {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True},]

print (week_log)

# Accessing Values Inside Nested Data

week_log [0] ["steps"] # Steps from the first day (Monday)
week_log [2] ["day"] # Day name of the third record (Wednesday)

week_log = [ {"day": "Monday", "steps": 9200, "protocol": "OMAD"}, {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"}, {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},]

# First day's step count 
print ("Monday steps:", week_log [0] ["steps"])

# Third day's protocol
print ("Wednesday protocol:", week_log [2] ["protocol"])

# Second day, all details
print ("Tuesday log:", week_log [1])

# Looping Through a List of Dictionaries
week_log = [ {"day": "Monday", "steps": 9200, "protocol": "OMAD", "cold_shower": True}, {"day": "Tuesday", "steps": 10500, "protocol": "2MAD", "cold_shower": True}, {"day": "Wednesday", "steps": 8800, "protocol": "OMAD", "cold_shower": True}, {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon", "cold_shower": False}, {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": False},]

for log in week_log: 
    status = "Goal hit" if log ["steps"] >= 8000 else "Below goal"
    print (log ["day"], "-", log ["steps"], "steps -", status, "," " Cold shower:", log ["cold_shower"])

# A Dictionary with a List as a Value

weekly_summary = { "week": 1, "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200], "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"], "cold_showers_completed": 6}

print ("Week:", weekly_summary ["week"])
print ("Total days tracked:", len (weekly_summary ["steps"]))
print ("First day steps:", weekly_summary ["steps"] [0])
print ("Averege steps:", sum (weekly_summary ["steps"])/ len (weekly_summary ["steps"]))

# A Real-World Pattern

clients = [ {"name": "James", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 80}, {"name": "Mwangi", "goal": "muscle gain", "weekly_sessions": 5, "bench_press_kg": 100}, {"name": "Sandra", "goal": "endurance", "weekly_sessions":3, "bench_press_kg": 50}, {"name": "Patrick", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 70},]

print ("Fat loss clients:")
for client in clients:
    if client ["goal"] == "fat loss":
        print ("-", client ["name"], "| Bench:", client ["bench_press_kg"], "kg| Sessions:", client ["weekly_sessions"])

# EXERCISE

week_log = [{"day": "Monday", "steps": 9200, "protocol": "OMAD"}, {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"}, {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"}, {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon"}, {"day": "Friday", "steps": 7600, "protocol": "OMAD"},]

total = 0
for log in week_log: 
    print (log ["day"], "|", log ["steps"], "steps |", log ["protocol"])
    total += log ["steps"]

average = total / len (week_log)
print ()
print ("Average steps:", average)