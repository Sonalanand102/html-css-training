# Note : the number of variables must match the number of elements unless we use extended unpacking with *.

# person = ("Rahul", 25, "Hyderabad")

# name, age, city = person

# print(name)
# print(age)
# print(city)

numbers = (10, 20, 30, 40)
# Note : *middle will contain all the middle values inside a list.
a, *middle, b = numbers

print(a)
print(middle)
print(b)