steps = 7500
body_weight_kg = 74.5
book = "Atomic Habits"
fasting = True

print ("Steps today Morning:", steps)
print ("My body weight today was:", body_weight_kg, "kg")
print ("Today I read chapter 5 of:", book)
print ("This evening I completed fasting:", fasting)

steps = 9200
body_weight_kg = 58.7
skill_of_the_day = "Editing"
cold_shower = True

print ("Steps today:", steps)
print ("Body weight:", body_weight_kg, "kg")
print ("Skill:", skill_of_the_day)
print ("Cold shower done:", cold_shower)

steps = 9200
body_weight = 58.7
skill = "Editing"
cold_shower = True

print (type(steps))
print (type(body_weight))
print (type(skill))
print (type(cold_shower))

steps = 9200
print ("Steps today:", steps)

steps = 9200
water_glasses = 8
skill = "Editing"
cold_shower = True

print (f"Steps: {steps}")
print (f"water:{water_glasses} glasses")
print (f"skill of the day:{skill}")
print (f"Cold shower:{cold_shower}")
print (f"You walked{steps} steps and drank {water_glasses} glasses of water.")

steps = 7200
print ("Morning count:", steps)

steps = 9400 # update the variable
print ("End of day:", steps)

steps = steps + 600 # add 600 to the current value
print ("After evening walk:", steps)

steps_as_string = "9400" # this is not a str, not a number
steps_is_int = int(steps_as_string)  # now it is an int

print (type(steps_as_string)) # <class 'str'>
print (type(steps_is_int)) # <class 'int'>

# You can now do maths with it 
target = 10000
gap = target - steps_is_int
print (f"You need {gap} more steps to hit your target.")

name = "Rhoney"
steps = 7500
hours_of_sleep = 7.5
water_glasses = 8
cold_shower_completed = True
skill = "AI Masterclass"

print (f"Name: {name}")
print (f"Steps: {steps} steps walked today")
print (f"Hours of sleep: {hours_of_sleep}")
print (f"Water glasses: {water_glasses}")
print (f"Cold shower completed: {cold_shower_completed}")
print (f"Current skills being learned: {skill}")

print (type(name))
print (type(steps))
print (type(hours_of_sleep))
print (type(water_glasses))
print (type(cold_shower_completed))
print (type(skill))

# You can now do maths with it
target = 10000
gap = target - steps
print (f"You need {gap} more steps to reach your target.")