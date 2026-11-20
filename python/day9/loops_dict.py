# Note : iterating over a dictionary directly gives its keys by default.

employee = {
    "name": "Rahul",
    "age": 25,
    "department": "IT"
}

for key in employee:
    print(key)

for value in employee.values():
    print(value)

# items() returns pairs that can be unpacked into two variables.

for key, value in employee.items():
    print(f"{key} : {value}")
