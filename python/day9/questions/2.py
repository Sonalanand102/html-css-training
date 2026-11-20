# An institute offers two courses: Python and Java.

# We have separate student lists for each course. Find the students who enrolled in both courses.

python_students = {
    "Rahul",
    "Priya",
    "Aman",
    "Sneha"
}

java_students = {
    "Priya",
    "Aman",
    "Rohit",
    "Neha"
}

print(python_students.intersection(java_students))
print(python_students & java_students)

# Students enrolled only in Python.

print(python_students - java_students)

# Students enrolled only in Java.

print(java_students - python_students)

# Students enrolled in either course.

print(java_students | python_students)


