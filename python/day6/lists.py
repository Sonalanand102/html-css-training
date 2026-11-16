"""
list : A list is an ordered, mutable collection of elements in Python.

properties:

1. Ordered: Elements maintain their positions.

2. Mutable: We can modify, add and remove elements.

3. Allows duplicates: The same value can appear multiple times.

Note : Lists are created using square brackets [].

"""

# students = ["Rahul", "Priya", "Aman", "Sneha"]
# numbers = [10, 20, 30, 40]
# prices = [10.5, 20.75, 30.25]
# data = ["Rahul", 25, 45000.50, True]



# print(students)
# print(numbers)
# print(prices)
# print(data)

# print(type(students))

# students = []

# print(students)

#  ======================================= 

# fruits = ["Apple", "Banana", "Mango"]

# fruits[1] = "Orange"

# print(fruits)

# ============ append() =============
# Adds one element to the end of the list.

print("Append Function.")

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

# ============ insert() =============
# Adds an element at a specific position.

print("Insert Function.")

fruits = ["Apple", "Banana"]

fruits.insert(1, "Orange")

print(fruits)

# ============ extend() =============
# Adds multiple elements from another iterable to the end of a list.

print("Extend Function.")

fruits = ["Apple", "Banana"]

fruits.extend(["Mango", "Orange"])

print(fruits)

# Note : 
# append() adds its argument as one element.
# extend() adds each element from the iterable separately.

# ============ remove() =============
# Removes the first occurrence of a specified value.

print("Remove Function.")

fruits = ["Apple", "Banana", "Mango", "Banana"]

fruits.remove("Banana")

print(fruits)

# # ============ pop() =============
# Removes and returns an element by index. If no index is provided, it removes the last element.
print("Pop Function.")

fruits = ["Apple", "Banana", "Mango"]

removed = fruits.pop(1)

print(fruits)
print(removed)

# # ============ clear() =============
# Removes all elements.

print("Clear Function.")

fruits = ["Apple", "Banana", "Mango"]

fruits.clear()

print(fruits)

# del statement 

print("del Statement.")

fruits = ["Apple", "Banana", "Mango"]

del fruits[1]

print(fruits)

# ============ sort() =============
# Sorts list in place

print("Sort Function in ascending order.")
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)

print("Sort Function in descending order.")

numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)

# ============ Reverse() =============
# Reverses list in place

print("Reverse Function.")
numbers = [40, 10, 30, 20]

numbers.reverse()

print(numbers)

# ============ index() =============
# Returns the index of a value

print("Index Function.")

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))

# ============ count() =============
# Counts occurrences

print("Count Function.")

numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))

# ============ copy() =============
# Creates a shallow copy

print("Copy Function.")

fruits = ["Apple", "Banana", "Mango"]

new_fruits = fruits.copy()

print("Original List:", fruits)
print("Copied List:", new_fruits)

# ============ len() =============
# Returns the number of elements

print("Len Function.")

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))

# sort() and sorted()
# sorted() returns a new sorted list, whereas sort() modifies the original list.

numbers = [30, 10, 20]



print(sorted(numbers))
print(numbers)

# max(), min()
