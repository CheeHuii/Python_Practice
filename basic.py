# _________Lesson 1____________#

# Print
print("Hello World!")
print("This print a line to console.")

# A comment!
# Yes, this is a comment for me and you to read.


# _________Lesson 2____________#
# Variables (strings, integers, float, boolean)
# Strings
first_name = "Chee Hui"
family_name = "Loh"

# Integers
age = 25

# Float
working_experience = 1.5

# Boolean
single = True

# f mean format, f-string, allow variable in {}
print(f"My name is {first_name}")
print(f"I am {age} years old.")
print(f"I have {working_experience} years of working experience.")
print(f"Am I single? {single}")

# if else statement
if single:
    print(":(")
else:
    print(":)")

# _________Lesson 3____________#
# Type casting (Converting variable from one type to another)

# Return type of variable
print(type(first_name))

# Casting start here
f_age = float(age)
print(f_age)
f_age = str(age)
print(f_age)
f_age = bool(age)
print(f_age)

single = str(single)
print(single)
# Strings can be concatenated
print(single +" "+ first_name)

# All number behind decimal ignore when cast to int
example_flaot = 3.99
example_float = int(example_flaot)
print(example_float)

# Cannot convert string to numbers
# family_name = float(family_name)
# print(family_name)

# Bool return True if not empty variable
f_name = bool(first_name)
print(f_name)
empty_string = ""
empty_string = bool(empty_string)
print (empty_string)

#__________Lesson 4__________#
# User input
# User input always in string.
user_input = input("Questions in terminal goes here: ")
user_number = input("Type me a random number: ")

# without casting to int returns error
user_number = int(user_number) + 1

# Then user_input can be used as strings
print(f"Bro u typed {user_input}")
print(f"Your number is {user_number}")