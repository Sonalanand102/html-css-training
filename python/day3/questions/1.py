"""
Input: Age.
Condition: Age must be at least 18.
Output: Eligible or not eligible.

"""

age = int(input("Enter your age:"))

result = "Eligible" if age>=18 else "Not Eligible"

print(result)