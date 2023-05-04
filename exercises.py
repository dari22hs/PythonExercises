"""
Here are some simple exercises to practice with Python.
"""
# 1) Write a Python program to print the Fibonacci sequence up to n numbers, where n is provided by the user.
n = int(input("Enter number: "))

# First two numbers of Fibonacci sequence
a, b = 0, 1

# Check if n is valid
if n <= 0:
    print("Invalid input.")
elif n == 1:
    print(a)
else:
    # Print the first two numbers
    print(a, b, end=" ")
    
    # Generate Fibonacci sequence
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

# 2) Write a Python program to check whether a given number is a prime number or not.
number = int(input("Enter number: "))

if number > 1:
    for i in range(2,int(number**0.5)+1):
        if (number % i) == 0:
            print(f"{number} is not a prime number.")
            break
        else:
            print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")