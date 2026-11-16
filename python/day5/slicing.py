"""
Slicing : String slicing allows us to extract a portion of a string.

syntax : string[start:stop:step]

start: Starting index, included.
stop: Ending index, excluded.
step: How many positions to move each time.

"""

word = "PYTHON"

print(word[0:3])
print(word[:3])
print(word[1:])

# Negative slicing

word = "PYTHON"

print(word[-4:-1])

# step slicing

word = "PYTHON"

print(word[::2])

word = "PYTHON"

print(word[::-1])
