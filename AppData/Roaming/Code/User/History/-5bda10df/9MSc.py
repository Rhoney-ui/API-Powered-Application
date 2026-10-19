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