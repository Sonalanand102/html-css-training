# Factorial of a Number

n = 10
factorial = 1

if n > 0:
    for i in range(1, n+1):
        factorial *= i
    
    print(f"Factorial of {n}: {factorial}")
else:
    print("Factorial is no defined for negative numbers.")

