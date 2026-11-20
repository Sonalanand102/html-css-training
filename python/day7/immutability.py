# Immutibility : 

# tuple elements cannot be reassigned.

# Note : a tuple can contain a mutable object such as a list. The list itself can still be modified.

# employee = ("EMP101", "Rahul", 25)

# employee[0] = "EMP102"

# print(employee)


data = (10, [20, 30], 40)

data[1].append(50)

print(data)