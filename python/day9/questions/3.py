# Create a Python program that stores a student's name, age, course and marks using a dictionary.

# The program should:
# 1. Display student details.
# 2. Update the student's marks.
# 3. Add a new field called city.
# 4. Display all the updated information.

name = input("Enter student name:")
age = int(input("Enter student age:"))
course = input("Enter Course name:")
marks = int(input("Enter students marks: "))

student = {
    "name" : name,
    "age" : age,
    "course" : course,
    "marks": marks
}

print("Student Details:")

for key, value in student.items():
    print(f"{key} : {value}")

new_marks = int(input("Enter updated marks:"))

student["marks"] = new_marks

city = input("Enter city name: ")

student["city"] = city

print("Student Updated Details:")

for key, value in student.items():
    print(f"{key} : {value}")

