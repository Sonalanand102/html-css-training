# def function_name(will contain parameters):
    # statements
    # function body

# Note : in order to execute a function you need to call the function by writing function_name followed by paenthesis and passing the argumentsif there is any whenever required.
# Types of functions:
# 1. Built-in functions :
# print("Hello")
# len("Python")
# type(100)
# max(10, 20, 30)
# min(10, 20, 30)
# sum([10, 20, 30])

# 2. User-defined functions : These are functions created by programmers according to their requirement.

# Parameter : A variable specified in the function definition. 
# Argument: The actual value passed when calling the function.

# def greet():
#     print("Hello, world!")
#     print("Welcome to python programming.")

# greet()

# def calculate_square(number = 5):
#     print(number * number)

# # user_number = int(input("Enter a number: "))

# calculate_square(9)

# # Note : We can also give default value to a parameter while defining a function like def greet(name = "") here the default value will be an empty string.

# def greet(name = ""):  # name is parameter
#     print("Hello", name)

# greet("Chandini")    # Rahul is argument

# def add_numbers(a, b):
    
#     result = a + b
#     print(f"{a} + {b} = {result}")

# add_numbers(10, 20)

# def greet():
#     print("Hello, world!")
#     print("Welcome to python programming.")

# Note : "return" sends the result back to the place where the function was called. 
# We can store that result in a variable, perform more calculations with it, or pass it to another function."

# def add(a, b):
#     print(a + b)
#     result = a+b
#     return result

# print("Result:", add(10, 20))

# Differnce b/w print and return 

# print : Displays output

# return : Sends a value back to the caller

# def add(a, b):
#     return a + b

# def multiply(number):
#     return number * 2

# result = add(10, 20) # 30

# final_result = multiply(result) # 60

# print(final_result)

# function immediately exits when it executes return.
# The print statement below it is unreachable.

# def example():
#     return 10
#     print("Hello")

# print(example())

# Python allows a function to return multiple values.
# that Python packages these values into a tuple.

def calculate(a, b):
    total = a + b
    difference = a - b
    product = a * b

    return total, difference, product

result_total, result_difference, result_product = calculate(20, 10) # (30, 10, 200)

print(result_total)

result = calculate(20, 10) #(30, 10, 200)

print(result[0])
