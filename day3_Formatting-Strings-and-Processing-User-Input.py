# 1) Using the variable below, print "Hello, world!".
greeting = "Hello, world!"
print("{}".format(greeting))

greeting = "Hello, world"
print(f"{greeting}!")

greeting = "Hello, world"
print(greeting + "!")

# 2) Ask the user for their name, and then greet them with their name.
#   using their name as part of the greeting. The name should be in title case, 
#   and shouldn't be surrounded by any excess white space.
name = input("Please enter your name: ").strip().title()
print(f"Hello, {name}!")

# 3) Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
age = 29
print("I am " + str(age))

# 4) Format and print the information below using string interpolation.
title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}), directed by {director}")
