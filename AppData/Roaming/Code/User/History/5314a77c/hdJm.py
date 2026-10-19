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
    print (log ["day"], "-", log ["steps"], "steps -", status)

cold_shower = True 
print (log ["day"], "-", log ["steps"], log ["cold_shower"]) if True 
if cold_shower = false, else False