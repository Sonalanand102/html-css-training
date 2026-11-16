# Accept five numbers from the user, store them in a list, and find the maximum and minimum values.

user_list = []

for i in range(5):
    num = int(input(f"Enter {i} number:"))
    user_list.append(num)

print("Maxium:", max(user_list))
print("Minimum:", min(user_list))
