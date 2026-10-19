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