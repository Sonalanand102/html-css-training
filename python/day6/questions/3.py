# Accept a sentence from the user and count how many vowels it contains.

sentence = input("Enter a string: ").lower()


count = 0

for char in sentence:

    if char in "aeiou":
        count += 1

print("Total vowels", count)
