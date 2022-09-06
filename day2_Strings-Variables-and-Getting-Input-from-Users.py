# 1) Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("What is your name? ")
age = input("What is your age? ")
print("Your name is " + name + " and your age is " + age)
# 2) Investigate what happens when you try to assign a value to a variable that you've already defined. 
#    Try printing the variable before and after you reuse the name.
x = 5
x = 7
print(x)
x = 5
print(x)
x = 7
# 3) Below you’ll find some code with a number of errors. 
#    Try to go through the program line by line and fix the issues in the code.
hourly_wage = input("Please enter your hourly wage: ")
print("Hourly wage: ")
print(hourly_wage)
hours_worked = input("How many hours did you work this week? ")
print("Hours worked: ")
print(hours_worked)