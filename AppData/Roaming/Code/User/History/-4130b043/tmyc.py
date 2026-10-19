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
steps_is_int = int(steps_as_string) # now it is an int