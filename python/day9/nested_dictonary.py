employees = {
    "EMP101": {
        "name": {
            "first_name" : "Rahul",
            "last_name" : "Kumar"
        },
        "age": 25,
        "department": "IT"
    },

    "EMP102": {
        "name": {
            "first_name" : "Priya",
            "last_name" : "Kumari"
        },
        "age": 23,
        "department": "HR"
    }
}

employees.items()

print(employees["EMP101"]["name"]["last_name"])

print(employees["EMP102"]["department"])

for emp_id, details in employees.items():

    print("Employee ID:", emp_id)

    print("Name:", details['name']["first_name"], details["name"]["last_name"])

    print("Age:", details["age"])

    print("Department:", details["department"])

    print("------------------")