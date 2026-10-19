# CREATING YOUR FIRST LIST

daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
print (daily_habits)

# ACCESSING ITEMS BY INDEX

daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
print (daily_habits [0]) # First item
print (daily_habits [2]) # Third item
print (daily_habits [4]) # Last item

# NEGATIVE INDEXING

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print ("Last day:", weekly_steps [-1])
print ("Second to last:", weekly_steps [-2])
print ("First day:", weekly_steps [-7])

# GETTING THE LENGTH OF A LIST 

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print ("Days tracked:", len(weekly_steps))

skills = ["welding", "tiling", "upholstery", "phone repair", "copywriting"]
print ("Skills in list:", len (skills))

# LOOPING THROUGH A LIST

daily_habits = ["8 glasses water", "8000 steps", "cold shower", "OMAD fast", "workout"]
for habit in daily_habits: 
    print ("Habit:", habit)

# COMBINE THE LOOP WITH A CONDITION

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
for steps in weekly_steps:
    if steps >= 10000:
        print (steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print (steps, "steps - Goal hit")
    else:
        print (steps, "steps - Below goal")

# CHECKING IF A VALUE IS IN A LIST

skills_learned = ["welding", "tiling", "copywriting", "phone repair"]

if "welding" in skills_learned:
    print ("Welding is in the list.")
if "beekeeping" not in skills_learned:
    print ("Beekeeping not found. Add it to the list")

# CHANGING AN ITEM IN A LIST

fasting_protocols = ["OMAD", "2MAD", "16:8", "Autophagy Marathon"]
print ("Before:", fasting_protocols)

# Update the third item (index 2)
fasting_protocols [2] = "Extended 72hr"
print ("After:", fasting_protocols)

# EXERCISE
week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

print ("=== EXERCISE ===")
for steps in week_steps: 
    if steps >= 8000:
        print (steps, "- Goal hit")
    else: 
        print (steps, "- Below goal")

print ("Days tracked: ", len(week_steps))