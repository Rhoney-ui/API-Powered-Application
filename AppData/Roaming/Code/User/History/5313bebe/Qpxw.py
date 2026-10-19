# LISTING METHODS: ADDING, REMOVING & SORTING

# Adding items: append () and insert ()

skills = ["welding", "tiling", "upholstery"]
print ("Before:", skills)

skills.append ("phone repair")
print ("After:", skills)

skills.append ("graphic design")
print ("Final:", skills)

# Insert ()

skills = ["welding", "tiling", "upholstery"]
print ("Before:", skills)

#insert "copywriting" at position 1 (second slot)
skills.insert (1, "copywriting")
print ("After:", skills)

# Removing Items: remove() and pop()

habits = ["8 glasses water", "cold shower", "OMAD fast", "workout", "cold shower"]
print ("Before:", habits)

habits.remove ("cold shower")
# Removes only the first one
print ("After:", habits)

# Pop

weekly_steps = [9200, 10500, 8800, 11000, 7600]
print ("Before:", weekly_steps)

removed = weekly_steps.pop()
# Removes last item
print ("Removed:", removed)
print ("After:", weekly_steps)

removed2 = weekly_steps.pop (1) # Removes item at index 1
print ("Removed:", removed2)
print ("After:", weekly_steps)

# SORTING: sort() and reverse()
# Sort ()

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
print ("Unsorted:", weekly_steps)

weekly_steps.sort ()
print ("Sorted low to high:", weekly_steps)

# Sort high to low by passing 
reverse = True
weekly_steps.sort (reverse = True)
print ("Sorted high to low:", weekly_steps)