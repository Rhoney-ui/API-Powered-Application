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
steps = 8600

if steps >= 10000:
    print ("Excellent. 10,000 steps exceeded.")
elif steps >= 8000:
    print ("On target. 8,000 steps hit.")
elif steps >= 5000:
    print ("Halfway. Below target but moving.")
else: 
    print ("Below 5,000. Today was sedentary.")