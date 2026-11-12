"""
Accept a user's first name, last name and city. Display a personalized welcome message.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")

full_name = first_name + " " + last_name

print("Hello, " + full_name + " from " + city + "! Welcome to the program.")

print(f"Hello, {full_name} from {city}! Welcome to the program.")

name = "chandni"

print("Hello", name)
print("Hello " + name)
print(f"Hello, {name}")