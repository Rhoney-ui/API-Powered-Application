# WORKING WITH CSV FILES
# Reading CSV with csv.reader

import csv
import io

# Simulated CSV content 
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)

# TRY IT: Skip The Header

print()
print("--- SKIP THE HEADER ---")
print()
import csv
import io

csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)
next(reader) # Skip header row

for row in reader:
    name, phone, skill, city = row
    print(f"{name} | {skill} | {city}")

# Reading with DictReader

print()
print("--- Reading with DictReader ---")
print()
import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = 'Goal hit' if steps >= 8000 else 'Below goal'
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")
