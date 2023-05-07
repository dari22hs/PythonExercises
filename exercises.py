"""
Here are some simple exercises to practice with Python.
"""
#** 1) Write a Python program to print the Fibonacci sequence up to n numbers, where n is provided by the user.
# n = int(input("Enter number: "))

# # First two numbers of Fibonacci sequence
# a, b = 0, 1

# # Check if n is valid
# if n <= 0:
#     print("Invalid input.")
# elif n == 1:
#     print(a)
# else:
#     # Print the first two numbers
#     print(a, b, end=" ")
    
#     # Generate Fibonacci sequence
#     for i in range(2, n):
#         c = a + b
#         print(c, end=" ")
#         a, b = b, c

#** 2) Write a Python program to check whether a given number is a prime number or not.
# number = int(input("Enter number: "))

# if number > 1:
#     for i in range(2,int(number**0.5)+1):
#         if (number % i) == 0:
#             print(f"{number} is not a prime number.")
#             break
#         else:
#             print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")
    
#** 3) Write a Python function to find the highest and lowest number in a list.


# def find_max_min():
#     myList = [0, 2, 4, 84, 54, 97, -18, -51]
#     theMax = max(myList)
#     theMin = min(myList)
#     print(f"The highest number in the list is {theMax}, and the lowest is {theMin}.")
  
  
# find_max_min()

#** 4) Write a Python function that takes a list of numbers and returns a new list containing only the even numbers.


# def get_even_numbers():
#     myList = [0, 2, 4, 84, 54, 97, -18, -51, 12, 98]
#     print(f"Original list: {myList}")
#     evenNumberList = []
#     for number in myList:
#         if number % 2 == 0:
#             evenNumberList.append(number)
#     return evenNumberList


# print(f"Even numbers extracted: {get_even_numbers()}")

#** 6) Write a Python function to check whether a string is a palindrome or not


# def check_palindrome(word):
#     word = ''.join(char for char in word.lower() if char.isalnum())
#     return word == word[::-1]


# word = input("Enter a word to check if it's a palindrome: ")
# print(check_palindrome(word))

#** 7) Write a Python program that accepts a string and calculate the number of digits and letters in it.


# def count_digits_letters(myString):
#     digits = 0
#     letters = 0
#     for char in myString:
#         if char.isdigit():
#             digits += 1
#         elif char.isalpha():
#             letters += 1
    
#     return digits, letters


# myString = input("Enter a string: >> ")
# digits, letters = count_digits_letters(myString)
# print(f"Number of digits: {digits}\nNumber of letters: {letters}")

#** 8) Write a Python function to reverse a string.


# def reverse_string(myString):
#     return myString[::-1]


# myString = input("Enter a string: >> ")
# print(f"String reversed: {reverse_string(myString)}")
    
#** 9) Write a Python program that accepts a sentence and calculates the number of uppercase letters and lowercase letters.


# def count_upper_lower(myString):
#     upper = 0
#     lower = 0
#     for char in myString:
#         if char.isupper():
#             upper += 1
#         elif char.islower():
#             lower += 1
#     return upper, lower


# myString = input("Enter a string: >> ")
# upper, lower = count_upper_lower(myString)
# print(f"Number of uppercase letters: {upper}\nNumber of lowercase letters: {lower}")

#** 10) Write a Python program that accepts a string and returns the number of times each word appears in the string


# def count_words(myString):
#     word_list = myString.split()
#     word_freq = {}
#     for word in word_list:
#         if word in word_freq:
#             word_freq[word] += 1
#         else:
#             word_freq[word] = 1
#     return word_freq


# myString = input("Enter a string: >> ")
# word_freq = count_words(myString)
# for word, freq in word_freq.items():
#     print(f"{word}: {freq}")

#** 11) Write a Python program to find the factorial of a given number.


# def find_factorial(number):
#     if number == 0:
#         return 1
#     else:
#         return number * find_factorial(number - 1)
    

# number = int(input("Enter a number: >> "))
# print(f"The factorial number of {number} is {find_factorial(number)}")

#** 12) Write a Python program to find the sum of the digits of a given number.


def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum


number = int(input("Enter a number: >> "))
print(f"The sum of the digits of {number} is: {sum_digits(number)}")


