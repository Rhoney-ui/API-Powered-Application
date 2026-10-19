# Introduction to NumPy
# What Is a NumPy Array?

# Creating Arrays
# CREATE NUMPY ARRAYS

import pip
import numpy as np

print()
print("=== CREATE NUMPY ARRAYS ===")
print()

# From a Python list
steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
print("steps array:", steps)
print("type:", type(steps))
print("dtype:", steps.dtype)
print("shape:", steps.shape)

# Zeros and ones
print("\nnp.zeros(5):", np.zeros(5))
print("np.ones(5):", np.ones(5))

# Range of numbers
print("np.arange(1, 8):", np.arange(1, 8))

# Evenly spaced
print("np.linspace(0, 1, 5):", np.linspace(0, 1, 5))

# Vectorized Operations
# VECTORIZED MATH

import pip
import numpy as np

print()
print("=== VECTORIZED MATH ===")
print()

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal = 10000

# All at once, no loop needed
deficit = steps - goal
print("Steps vs 10k goal:", deficit)

# Percentage of goal achieved
pct = (steps / goal * 100).round(1)
print("Percent of goal:", pct)

# Boolean mask: which days hit the goal?
hit = steps >= goal
print("Hit goal:", hit)
print("Days hitting goal:", steps[hit])

# Statistical Functions
# STATISTICAL ANALYSIS

import pip
import numpy as np

# 4 weeks of daily steps (28 days)
steps_28 = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])

print(f"28-day step analysis")
print(f" Mean: {np.mean(steps_28):,.0f}")
print(f" Median: {np.median(steps_28):,.0f}")
print(f" Std dev: {np.std(steps_28):,.0f}")
print(f" Min: {np.min(steps_28):,}")
print(f" Max: {np.max(steps_28):,}")
print(f" Total: {np.sum(steps_28):,}")
print(f" 75th pctile: {np.percentile(steps_28, 75):,.0f}")
print(f" Days 10k+: {np.sum(steps_28 >= 10000)}/28")
