# READING AND WRITING FILES

# Writing to a File

# In VS Code, this creates a file on your computer:
with open("daily_log.txt", "w") as f:
    f.write("Steps: 9200\n")
    f.write("Water: 8 glasses\n")
    f.write("Protocol: OMAD\n")
    f.write("Cold shower: Yes\n")

# SIMULATE WRITING A FILE

import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print ("--- WRITING A FILE SIMULATION ---")

print("File written.Contents:")
print(file_content.getvalue())

# READING A FILE
# In VS Code, this reads a file from your computer:
with open("daily_log.txt", "r") as f:
    content = f.read()
    print(content)

# SIMULATE READING A FILE
import io
# Simulate file content
file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

# Simulate reading the whole file
f = io.StringIO(file_data)
content = f.read()

print ("--- SIMULATION READING THE WHOLE FILE ---")
print("Full file content:")
print(content)

# READING LINE BY LINE
import io

file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
"""

f = io.StringIO(file_data)
lines = f.readlines()

print ("--- READING BY LINE ---")
print(f"Number of lines:{len(lines)}")
print()
for line in lines:
    line = line.strip() # Remove new line character at end
    print("Line:", line)

# APPENDING TO A FILE

# SIMULATE APPENDING

import io

# Start with existing content
file_data = "Steps: 9200\nWater: 8 glasses\nProtocol: OMAD\n"

# Simulate append
file_data += "Pages read: 30\n"
file_data += "Workout: bench press 5x5 at 80kg\n"

print ("--- APPENDING SIMULATION ---")
print("File after appending:")
print(file_data)

# PROCESSING FILE DATA

# PARSE LINES INTO A DICTIONARY

import io

file_data = """Steps: 9200
Water: 8
Protocol: OMAD
Cold Shower: Yes
Sleep Hours: 7.5
Pages read: 30
"""

log = {}
f = io.StringIO(file_data)
for line in f:
    line = line.strip()
    if ":" in line:
        key, value = line.split(":", 1)
        log[key.strip()] = value.strip()

print ("--- PARSE LINES INTO A DICTIONARY ---")

print("Parsed log:")
for key, value in log.items():
    print(f" {key}: {value}")

# EXERCISE
import io
# Simulated file: one line per day with step count
weekly_data = """Monday: 9200
Tuesday: 7500
Wednesday: 10500
Thursday: 8800
Friday: 6900
Saturday: 11000
Sunday: 9600
"""

goal = 8000
days_on_goal = 0

print ()
print ("--- EXERCISE - SIMULATION CODE ---")

f = io.StringIO(weekly_data)
for line in f:
    line = line.strip()
    if ":" in line:
        day, steps_str = line.split(":", 1)
        steps = int(steps_str.strip())
        status = "Goal hit" if steps >= goal else "Below goal"
        print(f"{day}: {steps} steps - {status}")
        if steps >= goal:
             days_on_goal += 1

    print(f"\nDays on goal: {days_on_goal}/7")

# APPLIED EXAMPLE: CHICKEN FARM EGG COLLECTION LOG

# CHICKEN FARM: READ AND WRITE LOG

print ()
print ("--- EXERCISE (CHICKEN FARM EGG COLLECTION LOG ---)")
import io
# Daily egg collection log: 
pen, eggs_collected, feed_kg
farm_log = """Pen A, 240, 12
Pen B,185,10
Pen C,310,15
Pen D,92,8
Pen E,275,13
"""

total_eggs = 0
total_feed = 0
low_pens = []

f = oi.StringIO(farm_log)
for line in f:
    line = line.strip()
    if line:
        pen, eggs, feed =line.split(":")
        eggs = int(eggs)
        feed = int(feed)
        efficiency = eggs / feed
        status = "Good" if eggs >= 200 else "Low yield"
        print(f"{pen}: {eggs} eggs | {feed}kg feed | {efficiency:.1f} eggs/kg [{status}]")
        total_eggs += eggs
        total_feed += feed
        if eggs < 200:

low_pens.append(pen)

print(f"\nTotal eggs: {total_eggs}")
print(f"Total feed used: {total_feed}kg")
print(f"Pens needing attention: {','.join(low_pens)}")
