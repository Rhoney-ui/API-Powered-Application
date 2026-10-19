# PROJECT: FITNESS AND DISCIPLINE CALCULATOR

# Calculator 1: BMI 

print ()
print ("=== CALCULATOR 1: BMI ===")
import math

def calculate_bmi (weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round (bmi, 1)

def bmi_category (bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Test
weight = 84
height = 1.78
bmi = calculate_bmi (weight, height)
print (f"Weight : {weight} kg")
print (f"Height : {height} m")
print (f"BMI : {bmi}")
print (f"Status : {bmi_category(bmi)}")

# Calculator 2: Step Goal Checker

print ()
print ("=== CALCULATOR 2: STEP GOAL CHECKER ===")
def weekly_step_summary (steps_list, goal=8000):
    days_hit = len([s for s in steps_list if s >= goal])
    average = sum(steps_list) / len(steps_list)
    best = max(steps_list)
    worst = min(steps_list)

    return {
        "days_on_goal": days_hit,
        "total_days": len(steps_list),
        "average": round(average),
        "best_day": best,
        "worst_day": worst
    }

weekly = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
result = weekly_step_summary(weekly)

print("Step Summary:")
print(f" Days on goal : {result['days_on_goal']}/{result['total_days']}")
print(f" Average : {result['average']} steps")
print(f" Best day : {result['best_day']} steps")
print(f" Worst day : {result['worst_day']} steps")