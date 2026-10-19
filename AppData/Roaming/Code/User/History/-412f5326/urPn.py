# YOUR FIRST FOR LOOP
for day in range (5):
    print ("Step goal: 8,000 steps")

# WATCH I CHANGE EACH ROUND 
for day in range (5):
    print ("Day:", day, "- Step goal: 8,000 steps")

# COUNT FROM 1 TO 7: ONE WEEK OF DISCIPLINE
for day in range (1, 8):
    print ("Day", day, "- Step goal: 8,000 steps")

#TRY IT YOURSELF 
for day in range (1, 31):
    print ("Day", day, "- Step goal: 8,000 steps")

# YOUR FIRST WHILE LOOP: WATER TRACKER
glasses = 0

while glasses < 8:
    glasses = glasses + 1
    print ("Glass", glasses, "done.")

# BREAK: STOP WHEN TARGET IS HIT
daily_steps = [3200, 7100, 9800, 10500, 6400, 11200]
target = 10000

for steps in daily_steps:
    print (f"Checking: {steps} steps")
    if steps >= target:
        print (f"Target hit on this day: {steps} steps. Stopping search.")
        break

# CONTINUE: SKIP INVALID DAYS
daily_steps = [3200, 7100, 9800, 4100, 10500, 6400]
minimum = 7000

total = 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum:
        print (f"Skipping {steps} (below minimum)")
        continue # skip this day, go to next
    total += steps
    valid_days += 1

print (f"\nValid days: {valid_days}")
print (f"Total steps (valid_days): {total}")
print (f"Average: {total // valid_days}")

# EXERCISE
daily_steps = [8200, 5100, 11300, 6800, 9400, 4200,10100]
target = 8000

for steps in daily_steps:
    print (f"Checking: {steps} steps")
    if steps >= target:
        print (f"Target hit on this day: {steps} steps. Stopping search.")
        break

minimum = 5000

total = 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum:
        print (f"Skipping {steps} (below minimum)")
        continue # skip this day, go to next
    total += steps
    valid_days += 1

while steps < 8000:
    steps = steps + 1
    print ("Steps", steps, "done.")