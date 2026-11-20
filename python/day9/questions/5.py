# You are building an application that stores 100 employees. 
# Each employee has an 
# ID, name, age, department and salary. 
# How would you structure this information?


employee = []
for i in range(100):
    employee.append({
        "id" : i + 1,
        "name" : "",
        "age" : 0,
        "department" : "",
        "salary" : 0
    })

# print(employee)

employee[50]["name"] = "Sonal"

print(employee[50])

