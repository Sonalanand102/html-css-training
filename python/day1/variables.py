"""
Variable Naming Conventions in Python

1. Must start with a letter(a-z, A-Z) or underscore (_)
2. Cannot start with a number(0-9)
3. Cannot contain spaces or special characters like !, @, #, $, %, etc.
4. Can contain numbers after the first character.
5. Variable names are case-sensitive (age, Age, and AGE are three different variables)
6. Cannot use reserved keywords as variable names (e.g., if, else, while, for, etc.)

Note: Python commonly uses snake_case for variable names, which means using lowercase letters and underscores to separate words (e.g., my_variable_name).

"""



# variable_name = value

# name = "Rahul"
# age = 22
# salary = 25000.50
# is_employed = True


name, age, salary, is_employed = "Rahul", 22, 25000.50, True

a = b = c = 0



print("Name:", name)
print("Age:", age)
print("Salary:", salary)
print("Rahul is employed:", is_employed)

salary = 30000.75
print("Updated Salary:", salary)

value = 100 

print("Value:", value)

value = "Hello, World!"

print("Updated Value:", value)