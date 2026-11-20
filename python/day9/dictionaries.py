# Dictionary : A dictionary is a mutable collection that stores data in key-value pairs.

# Terminolgies : 
# Key: Identifies a particular value.
# Value: The information associated with that key.
# Key-value pair: A combination of a key and its corresponding value.

# Properties : 

# Key-value structure: Each entry has a key and a value.

# Mutable: We can add, update and delete entries.

# Unique keys: Duplicate keys are not maintained; a later assignment replaces the earlier value.

# Insertion ordered: Modern Python dictionaries preserve insertion order.

# Keys must be hashable: Strings, integers and tuples containing hashable elements can be keys. Lists and sets cannot be dictionary keys.

# Values can be of different types: Strings, integers, lists, tuples and even other dictionaries can be stored as values.


# Syntax : Dictionaries are created using curly braces {}.

# employee = {
#     "name": "Rahul",
#     "age": 25,
#     "employee_id": "EMP101",
#     "department": "IT",
#     "salary": 45000
# }

# print(employee)

# student = {
#     "name": "Rahul",
#     "age": 22,
#     "name": "Priya"
# }

# print(student)

# ============== access data ============
# use get() when a key might be missing and direct indexing when the key is expected to exist.

employee = {
    "name": "Rahul",
    "age": 25,
    "salary": 45000,
    # "department": "IT"
}

print(employee["name"])
print(employee["salary"])
# print(employee["department"])

print(employee.get("name"))
print(employee.get("department"))

# ============ add elements ============

employee = {
    "name": "Rahul",
    "age": 25
}

employee["department"] = "IT"

employee["salary"] = 45000

print(employee)

# =========== update dict values ============

employee = {
    "name": "Rahul",
    "age": 25,
    "salary": 45000
}

employee["salary"] = 50000

# update() modifies existing keys and adds new keys if they don't exist.

employee.update({
    "age": 26,
    "department": "IT"
})

print(employee)

# =========== pop() ==========
# Removes a key and returns its associated value.

employee = {
    "name": "Rahul",
    "age": 25,
    "salary": 45000
}

removed_salary = employee.pop("salary")

print(employee)
print(removed_salary)

# ============ popitem() =============
# Removes and returns the last inserted key-value pair.

employee = {
    "name": "Rahul",
    "age": 25,
    "salary": 45000
}

print(employee.popitem())

# ============= del ========
# Deletes a particular key-value pair.

del employee["age"]

print(employee)

# ========= clear() ========

employee.clear()

print(employee)

# ========== keys(), values(), items() =========
# keys : Returns all keys
# values : Return all values
# items : returns key-value pairs

# Note : these methods return dictionary view objects, which reflect changes to the dictionary.

student = {
    "name": "Priya",
    "age": 22,
    "course": "Python"
}


print(student.keys())

print(student.values())

print(student.items())