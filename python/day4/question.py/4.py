# Accept a positive integer N and calculate the sum of all natural numbers from 1 to N.

n = 3
total = 0

for i in range(1, n+1):
    total += i

print(f"Sum of {n} natural numbers: {total}")
