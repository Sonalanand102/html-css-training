
# Implicit Type Conversion : Python automatically converts certain values when performing compatible operations.

print("Implicit Type Conversion:")

a = 10
b = 5.5

result = a + b  # Implicitly converts 'a' to float before addition
print("Result of addition:", result)
print("Type of result:", type(result))

# Explicit Type Conversion : Python allows you to explicitly convert values from one data type to another using built-in functions.
print("\nExplicit Type Conversion:")

x = "10"
y = 5

# Convert string to integer
x = int(x)
result = x + y  # Now both values are integers
print("Result of addition:", result)
print("Type of result:", type(result))

# Convert integer to string

age = 25

age = str(age)

print(age)
print(type(age))

# Convert string to float

price = "99.50"

price = float(price)

print(price)
print(type(price))

