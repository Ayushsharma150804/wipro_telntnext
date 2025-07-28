# 1. Create a Python program that asks the user how far they want to travel.
# If they want to travel less than three miles, tell them to ride Bicycle.
# If they want to travel more than three miles, but less than three hundred miles, tell them to ride Motor-cycle.
# If they want to travel three hundred miles or more, tell them to drive Super-Car.
# Sample Output:
# How far would you like to travel in miles? 2500
# I suggest Super-Car to your destination

distance = float(input("How far would you like to travel in miles? "))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif 3 <= distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")


# 2. Build a Python program to calculate server operating cost.
# Hosting cost: $0.51 per hour
# Display:
# - Cost per day
# - Cost per week
# - Cost per month
# - How many days can one operate a server with $918?

hourly_rate = 0.51
hours_per_day = 24
days_per_week = 7
days_per_month = 30
budget = 918

cost_per_day = hourly_rate * hours_per_day
cost_per_week = cost_per_day * days_per_week
cost_per_month = cost_per_day * days_per_month
days_with_budget = budget / cost_per_day

print("\nServer Cost Calculations:")
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for {days_with_budget:.2f} days")
