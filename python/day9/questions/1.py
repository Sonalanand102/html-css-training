# A school has a list of student names, but some students appear multiple times because of duplicate registrations.

# Create a program that removes duplicate names.

students = [
    "Rahul",
    "Priya",
    "Aman",
    "Rahul",
    "Priya",
    "Sneha"
]

new_student_set = set(students)

ordered_student_list = list(dict.fromkeys(students))

print(new_student_set)
print(ordered_student_list)