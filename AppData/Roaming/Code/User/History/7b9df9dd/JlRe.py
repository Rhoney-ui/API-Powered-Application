# PROJECT: DRAGE TRACKER
# STEP 1: The Data

import csv
import io

csv_data = """name,score1,score2,score3
James Omondi,85,90,78
Sandra Weru,72,,88
Patrick Njiru,91,81,94
Grace Achieng,60,bad data,70
Brian kamau,55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    print(dict(row))