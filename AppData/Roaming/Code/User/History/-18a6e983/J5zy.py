# LIST COMPREHENSIONS AND LAMBDA

# List Comprehension

# The Problem: Building Lists with Loops

# STANDARD LOOP APPROACH

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = []
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)
        print(goal_days)