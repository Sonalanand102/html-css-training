#  =============== add() ===============
#  Adds one element.
fruits = {"Apple", "Banana"}

fruits.add("Mango")

print(fruits)

# ============= update() ==========
#  Adds multiple elements from an iterable.
fruits = {"Apple", "Banana"}

fruits.update(["Mango", "Orange"])

print(fruits)

# ========== remove() ============
# Removes an element; raises KeyError if absent

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)

# ============= discard() ===========
# Removes an element; does nothing if absent

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)

