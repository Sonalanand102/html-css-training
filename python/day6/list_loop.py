fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i,fruits[i])

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


students = [
    ["Rahul", 85],
    ["Priya", 90],
    ["Aman", 78]
]

# print(students)

print(students[0]) # ['Rahui', 85]
print(students[0][0]) # Rahul
print(students[0][1]) # 85

for student in students:
    print(f"Name : {student[0]}, Marks: {student[1]}")


