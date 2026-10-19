# FIRST IF STATEMENT
steps = 5000

if steps >= 8000:
    print ("Step target hit.")

print ("Daily check complete")

# IF + ELSE: STEP CHECK 
steps = 9000

if steps >= 8000:
    print ("Target hit. Well done.")
else:
    print (f"Target missed. You need {8000 - steps} more steps.")

# IF + ELIF + ELSE: GRADED STEP CHECK
steps = 3000

if steps >= 10000:
    print ("Excellent. 10,000 steps exceeded.")
elif steps >= 8000:
    print ("On target. 8,000 steps hit.")
elif steps >= 5000:
    print ("Halfway. Below target but moving.")
else: 
    print ("Below 5,000. Today was sedentary.")

# COMBINING CONDITIONS: DAILY DISCIPLINE CHECK
steps = 9200
water_glasses = 8
cold_shower = False
sleep_hours = 7

if steps >= 8000 and water_glasses >= 8:
    print ("Steps and water: both on target.")
else: 
    print ("Steps or water below target.")

if sleep_hours >= 7 and cold_shower: 
    print ("Sleep and cold shower: both done.")
else: 
    print ("Sleep or cold shower missed.")

# NESTED CONDITIONS: TRAINING SESSION CHECK
workout_done = True
weight_lifted_kg = 5200
personal_best_kg = 5000

if workout_done: 
    print ("Workout logged.")
    if weight_lifted_kg > personal_best_kg:
        print ("New personal best! Previous:", personal_best_kg, "kg")
        print ("New record:", weight_lifted_kg, "kg")
    else: 
            print ("Solid session. No new record today.")
    else: 
                print ("Rest day. No workout logged.")