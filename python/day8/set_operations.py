cricket = {"Rahul", "Priya", "Aman", "Sneha"}

football = {"Priya", "Aman", "Rohit", "Neha"}

# Union : A U B : Union combines all unique elements from both sets.

result = cricket.union(football)

result2 = cricket | football

print(result)
print(result2)

# Intersection : Intersection returns only the elements that are common to both sets.

result = cricket.intersection(football)

print(result)
print(cricket & football)

# Difference : Difference returns elements present in the first set but not in the second.
# Note: the order of the sets matters in difference operations.
print(cricket.difference(football))
print(cricket - football)

print(football - cricket)

#  Symmetric Difference : Returns elements that are in either set but not in both.

print(cricket.symmetric_difference(football))

print(cricket ^ football)

# memebership operators in sets

students = {"Rahul", "Priya", "Aman"}

print("Rahul" in students)

print("Sneha" not in students)