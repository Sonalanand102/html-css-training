# Types of argument : 

# 1. positional arguments
# 2. keyword arguments
# 3. default arguments
# 4. Keyword and positional arguments together
# 5. *args and **kwargs

# 1. positional arguments : Values are assigned to parameters according to their position.

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student("Rahul", 22)

# 2. Keyword argument : Instead of relying on position, we can specify parameter names.

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student(age=22, name="Rahul")

# 3. Default Argument : Sometimes we want to provide a default value to a parameter.

# def greet(name="Guest"):
#     print("Welcome", name)

# greet("Rahul")
# greet()

# # Note : Non-default parameters must come before default parameters.

# def student(name, age=18):
#     print(name, age)

# 4. Keyword and positional arguments together : 
# You can combine both, 
# but positional arguments must come before keyword arguments when calling a function.

# def employee(name, salary, city):
#     print(name, salary, city)

# employee("Rahul", salary=50000,  city="Hyderabad")

# 5. *args
# *args allows a function to accept any number of additional positional arguments.
# *args is a tuple

def add_numbers(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

print(add_numbers(10, 20))
print(add_numbers(5, 10, 15, 20, 25))

# 5. **kargs : **kwargs allows a function to accept any number of keyword arguments.
# kwargs is a dictionary.

def student_details(**student_data):
    print(student_data)

student_details(name="Rahul", age=22, course="Python")

def display_details(**details):

    for key, value in details.items():
        print(key, ":", value)

display_details(
    name="Rahul",
    age=22,
    city="Hyderabad",
    profession="Developer"
)

# ==================================
# Explain briefly that * and ** can also unpack existing collections when calling functions.
# - In a function definition, *args and **kwargs collect arguments.
# - In a function call, * and ** unpack collections.

def add(a, b):
    return a + b

numbers = {10, 20}

print(*numbers)

print(add(*numbers))

#  ===

def student(name, age):
    print(name, age)

details = {"name": "Rahul", "age": 22}

# for key, value in details.items():

# print(**details) === print(username = "rahul")

student(**details)

# =========

def details(*args, **kargs):
    print(args, kargs)

details("sonal", 25, 50000, email="sonalanand102@gmail.com", course = "python")