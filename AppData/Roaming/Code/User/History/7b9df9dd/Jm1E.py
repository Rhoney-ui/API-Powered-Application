# PROJECT: DRAGE TRACKER
# STEP 1: The Data

print()
print("=== THE DATA ===")
print()
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

# STEP 2: Parse Scores Safely

print()
print("=== STEP 2: Parse Scores Safely ===")
print()
def parse_score(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

# Test
print(parse_score("85"))
print(parse_score(""))
print(parse_score("bad data"))
print(parse_score(None))