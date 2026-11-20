numbers = (10, 20, 30, 20)

print(numbers.count(20))
print(numbers.index(30))

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
print(a | b)

student = {
    "name": "Rahul",
    "age": 22
}

student["age"] = 23

student["city"] = "Hyderabad"

print(student)

employee = {
    "name": "Priya",
    "salary": 50000,
}

# print(employee["department"])

print(employee.get("department", "Not Assigned"))

person = ("Aman", 25, "Developer")

name, age, role = person

print(name)
print(role)