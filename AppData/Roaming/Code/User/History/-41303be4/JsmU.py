morning_steps = 4200
afternoon_steps = 5000

# Addition
total_steps = morning_steps = afternoon_steps
print (f"Total steps: {total_steps}")

# Subtraction
steps_remaining = 10000 - total_steps
print (f"Steps to rach 10,000: {steps_remaining}")

# Multiplication
weekly_target = 8000 * 7
print (f"Weekly step target: {weekly_target}")

# Division
daily_average = 65000 / 7
print (f"Daily average this week: {daily_average}")

# Integer division, Modulo, and Power
total_steps = 65000
days = 7

# Clean whole number average (no decimal)
daily_average = total_steps // days
print (f"Daily average: {daily_average} steps")

# How many full sets of 1000 steps?
full_thousands = total_steps // 1000
print (f"Full thousands: {full_thousands}")

# Power: how many steps in 2 weeks squared?
print (f"8000 to the power of 2: {8000 ** 2}")

# Build a weekly training report
bench_press_sets = 5
reps_per_set = 12
weight_per_rep_kg = 80

total_reps = bench_press_sets * reps_per_set 
total_volume_kg = total_reps * weight_per_rep_kg
reps_per_minute = total_reps // 4 # assume 4 minutes of work time

print ("=== BENCH PRESS SESSION ===")
print (f"Sets: {bench_press_sets}")
print (f"Reps per set: {reps_per_set}")
print (f"Total reps: {total_reps}")
print (f"Weight per rep: {weight_per_rep_kg} kg")
print (f"Total volume lifted: {total_volume_kg} kg")
print (f"Reps per minute: {reps_per_minute}")

# Comparison Operators
steps = 9200
water_glasses = 6
sleep_hours = 7
fasting = "OMAD"

print (steps >= 8000)
# Did I hit my step target?
print (water_glasses == 8)
# Did I drink exactly 8 glasses?
print (sleep_hours < 6)
# Did I sleep under 6 hours?
print (fasting != "None")
# Am I on a fasting protocol?
print (steps > 10000)
# Did I exceed 10,000 steps?

# String Operations
# Joining text with +
first_name = "Amerix"
greeting = "Welcome, " + first_name + "."
print (greeting)

skill = "Welding"
message = "Today's skill is " + skill + "."
print (message)

# Exercise
number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
weight_per_rep_kg = 60
session_duration_minutes = 45

total_sets = sets_per_exercise * number_of_exercises
total_reps = total_sets * reps_per_set
total_volume = total_reps * weight_per_rep_kg
reps_per_minute = total_reps // 48

print ("=== CLIENT X WORKOUT ROUTINE ===")
print (f"Total sets: {total_sets}")
print (f"Total reps: {total_reps}")
print (f"Total volume: {total_volume} kg")
print (f"Reps per minute: {reps_per_minute}")
print (total_volume > 10000)
# Did I exceed 10,000 kg target? 