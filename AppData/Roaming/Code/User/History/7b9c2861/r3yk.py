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
file_data = "Steps: 
9200\nWater: 8
glasses\nProtocol: OMAD\n"

# Simulate append
file_data += "Pages read: 30\n"
file_data += "Workout: bench press 5x5 at 80kg\n"

print ("--- APPENDING SIMULATION ---")
print("File after appending:")
print(file_data)