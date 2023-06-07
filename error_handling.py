"""
Error handling basics.
Error handling in Python involves handling and managing exceptions that occur during the execution of a program. Exceptions are events that disrupt the normal flow of code execution and can occur due to various reasons, such as invalid input, file not found, network errors, and so on. Python provides a mechanism to catch and handle these exceptions, allowing you to gracefully handle errors and prevent your program from crashing.
"""
#** 1) Handling specific exception
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
#     print(f"Division result: {result}")
# except ZeroDivisionError:
#     print("Error. Can't divide by zero (0).")
# except ValueError:
#     print("Error. Invalid input.")

#** 2) Handling multiple exceptions
try:
    file = open("data.txt", "r")
    contents = file.read()
    file.close()
    print("File contents:", contents)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to access the file.")
except Exception as e:
    print("Error:", str(e))
