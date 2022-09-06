name = input("Please enter the employee's name: ").strip().title()
hourly_wage = input("What is their hourly wage? ")
hours_worked = input("How many hours have they worked this week? ")

earnings = float(hourly_wage) * int(hours_worked)

print(f"{name} earned ${earnings:.2f} this week.")