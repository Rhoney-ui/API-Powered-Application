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

# STEP 3: Calculate Average and Letter Grade

print()
print("=== STEP 3: Calculate Average and Letter Grade ===")
print()
def calculate_average(scores):
    valid = [s for s in scores if s is not None]
    if not valid:
        return None
    return round(sum(valid) / len(valid), 1)

def letter_grade(avg):
    if avg is None:
        return "N/A"
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Test
scores_a = [85, 90, 78]
scores_b = [72, None, 88]
scores_c = [60, None, None]

for s in [scores_a, scores_b, scores_c]:
    avg = calculate_average(s)
    print(f"Scores: {s} | Avg: {avg} | Grade: {letter_grade(avg)}")
