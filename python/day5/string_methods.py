"""
Note: Python provides built-in string methods to manipulate strings.

Commonly used string mehtods:

upper() - convert the string into uppercase
lower() - convert the string into lowercase
capitalize() - capitalize the first character of the entrie string 
title() - capitalize first character of each word 
strip() - Removes leading/trailing whitespace
lstrip() - Removes leading whitespace
rstrip()- Removes trailing whitespace
replace() - Replace a substring
split() - split string words into a list
find() - Return the first matching index or -1
count() - count occurrences of substring
startswith() - checks starting characters
endswith() - checks ending characters
isalpha() - Checks whether all characters are alphabetic
isdigit() - Checks whether all characters are digits
isalnum() - Checks whether all characters are alphanumeric

"""

# upper & lower

name = "Python Programming"

print(name.upper())
print(name.lower())

# capitalize & title
name = "python programming"

print(name.capitalize())
print(name.title())

# strip, lstrip & rstrip

email = "   user@gmail.com   "

print(email)
print(email.strip())
print(email.lstrip())
print(email.rstrip())

# replace

message = "I love Java"

updated_message = message.replace("Java", "Python")

print(updated_message)

# split

sentence = "Python is easy to learn"

words = sentence.split()

print(words)

# find

message = "I love Python"

print(message.find("Python"))
print(message.find("Java"))

# count

text = "banana"

print(text.count("na"))

text = "I love Python"

print(text.count("Python"))

# startswith & endswith

email = "user@gmail.com"

print(email.startswith("user"))
print(email.endswith(".com"))
print(email.isalnum())

# Note : The program give below will create a TypeError because strings are immutable.
# Immutable means that once a string is created, its individual characters cannot be changed in place.

"""
name = "Python"

name[0] = "J"
"""
name = "Python"

name = "J" + name[1:]

print(name)