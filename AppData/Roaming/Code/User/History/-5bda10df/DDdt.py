# Grouping and Aggregation

# BASIC GROUPBY

import pip
import pandas as pd

print()
print("=== BASIC GROUPBY ===")
print()

df = pd.DataFrame({
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD","2MAD", "OMAD", "OMAD"],
})

# Average steps per fasting protocol
grouped = df.groupby("protocol") ["steps"].mean().round(0)
print("Average steps by protocol:")
print(grouped)

print()
# Total steps per protocol
totals = df.groupby("protocol") ["steps"].sum()
print("Total steps by protocol:")
print(totals)

# Common Aggregation Functions
# MULTIPLE AGGREGATIONS

import pip
import pandas as pd

print()
print("=== MULTIPLE AGGREGATIONS ===")
print()

df = pd.DataFrame({
    "name": ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Sandra"],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Mombasa"],
    "steps": [9200, 10500, 8100, 11000, 7400, 10800, 9800, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 7.0, 8.5],
})

# Multiple aggregations on step by city
city_stats = df.groupby("city") ["steps"].agg(["mean", "max", "min", "count"]).round(0)
print("Steps statistics by city:")
print(city_stats)

# Grouping Multiple Columns at Once
# GROUP MULTIPLE COLUMNS

import pip
import pandas as pd

print()
print("=== GROUP MULTIPLE COLUMNS ===")
print()

df = pd.DataFrame ({
    "city": ["Nairobi", "Nairobi", "Mombasa", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Kisumu"],
    "protocol": ["OMAD", "2MAD", "OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "2MAD"],
    "steps": [9200, 10500, 8100, 11000, 9400, 10200, 7400, 8800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 7.5, 8.0, 9.0, 7.5],
})

# Average steps grouped by both city and protocol
breakdown = df.groupby(["city", "protocol"]) ["steps"].mean().round(0)
print("Average steps by city and protocol:")
print(breakdown)

# value_counts()
# COUNT UNIQUE VALUES

import pip
import pandas as pd

print()
print("=== COUNT UNIQUE VALUES ===")
print()

df = pd.DataFrame({
    "name": ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Grace", "Sandra", "James"],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD", "OMAD", "2MAD", "OMAD"],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Kisumu", "Mombasa", "Nairobi"],
})

print("Protocol distribution:")
print(df["protocol"].value_counts())

print("\nCity distribution:")
print(df["city"].value_counts())
