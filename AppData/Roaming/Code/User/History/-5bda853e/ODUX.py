# Filtering and Transforming Data
# Boolean Filtering

# FILTER ROWS 

import pip
import pandas as pd

print()
print("=== FILTER ROWS ===")
print()

df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Days where step goal was hit
goal_days = df[df["steps"] >= 10000]
print("Days with 10k+ steps:")
print(goal_days[["day", "steps", "protocol"]].to_string())

print()
# Days with less than 7.5 hours sleep
low_sleep = df[df["sleep_hr"] < 7.5]
print("Days with under 7.5 hours sleep:")
print(low_sleep[["day", "sleep_hr"]].to_string())

# Multiple Conditions

import pip
import pandas as pd

print()
print("=== MULTIPLE CONDITIONS ===")
print()

df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True],
})

# OMAD days with 10k+ steps
omad_goal = df[(df["protocol"] == "OMAD") & (df["steps"] >= 10000)]
print("OMAD days with 10k+ steps:")
print(omad_goal[["day", "steps", "protocol"]].to_string())

print()
# Days with either goal steps OR 8+ hours sleep
either = df[(df["steps"] >= 10000) | (df["sleep_hr"] >= 8.0)]
print("Days with 10k+ steps OR 8+ hrs sleep:")
print(either[["day", "steps", "sleep_hr"]].to_string())

# Filtering with .isin()
# FILTER WITH .ISIN()

import pip
import pandas as pd

print()
print("=== FILTER WITH .ISIN() ===")
print()

df = pd.DataFrame({
    "name": ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps": [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})

# Members from Nairobi or Mombasa
nbi_msa = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("Nairobi and Mombasa members:")
print(nbi_msa[["name", "city", "steps"]].to_string())