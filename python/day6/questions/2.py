# Write a program to check whether a given string is a palindrome.
# A palindrome is a word or sequence that reads the same forward and backward.

user_input = input("Enter a string:").lower()

# Madam

reversed_text = user_input[::-1]

if user_input == reversed_text:
    print("It's a palindrome")
else:
    print("not a palindrome")