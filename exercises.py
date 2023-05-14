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


# def sum_digits(number):
#     sum = 0
#     for digit in str(number):
#         sum += int(digit)
#     return sum


# number = int(input("Enter a number: >> "))
# print(f"The sum of the digits of {number} is: {sum_digits(number)}")

#** 13) Write a Python program to count the number of vowels in a given string.


# def count_vowels(myString):
#     vowels = set("aeiouAEIOU")
#     count = 0
#     for letter in myString:
#         if letter in vowels:
#             count += 1
#     return count


# myString = input("Enter a string: >> ")
# print(f"\nTotal vowels: {count_vowels(myString)}")

# # Counting each vowel individually
# myString = myString.lower()
# print(f"""
# Total 'A/a' vowels: {myString.count('a')}
# Total 'E/e' vowels: {myString.count('e')}
# Total 'I/i' vowels: {myString.count('i')}
# Total 'O/o' vowels: {myString.count('o')}
# Total 'U/u' vowels: {myString.count('u')}""")

#** 14) Write a Python program to find the second largest number in a list.


# def find_second_highest(list_of_numbers):
#     if len(list_of_numbers) > 1:
#         list_of_numbers.sort()
#         return list_of_numbers[-2]
#     else:
#         print("Fill your list at least with 2 elements!")
#         return None
        
# list_of_numbers = [117, 19, 22, 1990, 11, 94, 49, 13, 69, 77]
# print(f"Original list: {list_of_numbers}")
# print(f"The second highest number is: {find_second_highest(list_of_numbers)}")


#** 15) Write a Python program to find the common elements between two lists.


# def find_coincidences_in_lists(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     coincidences = set1.intersection(set2)
#     return list(coincidences)


# list1 = [19, 88, 91, 34, 65, 110, 38, 88, 34, 34, 10551]
# list2 = [1, 88, 91, 94, 25, 109, 19, 300, 10551, 784, 5]
# print(f"Coincidences in both lists: {find_coincidences_in_lists(list1, list2)}")

#** 16) Write a Python program to sort a list of tuples based on the second element of each tuple.


# def sort_tuple_by_second_element(list_of_tuples):
#     """
#     Function that sorts a list of tuples based on the second element of each tuple. Function 'sorted' is used as well as a lambda function as the 'key' parameter. This parameter is used to specify a function to be called on each element of the iterable that is being sorted. This function returns a value that is used to determine the order of the elements in the sorted result. The 'x' parameter represents each tuple in the list of tuples. The x[1] expression retrieves the second element of each tuple, which is what we want to use for sorting.
#     """
#     return sorted(list_of_tuples, key=lambda x: x[1])


# list_of_tuples = [(2, 4), (5, 3), (7, 15), (23, 4), (7,8), (1, 1)]
# print(f"Original list of tuples: {list_of_tuples}")
# print(f"Sorted list of tuples: {sort_tuple_by_second_element(list_of_tuples)}")

#** 17) Write a Python program to find the GCD (greatest common divisor) of two numbers.


# def find_gcd(num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return find_gcd(num2, num1%num2)


# num1 = int(input("Enter a number: >> "))
# num2 = int(input("Enter another number: >> "))
# print(f"The greatest common divisor of {num1} and {num2} is: {find_gcd(num1, num2)}")

#** 18) Write a Python program to find the sum of all prime numbers between 1 and n (where n is provided by the user)


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# n = int(input("Enter a number: >> "))
# sum_primes = 0
# for i in range(2, n+1):
#     if is_prime(i):
#         sum_primes += i
        
# print(f"The sum of all primes between 1 and {n} is: {sum_primes}")

#** 19) Write a Python program to find the length of the longest consecutive sequence of a given list of integers.


def find_longest_consecutive_seq(myList):
    myList.sort()
    longest_seq = 0
    current_seq = 0
    for i in range(1, len(myList)):
        if myList[i] == myList[i-1] + 1:
            current_seq += 1
        else:
            longest_seq = max(longest_seq, current_seq)
            current_seq = 1
    longest_seq = max(longest_seq, current_seq)
    return longest_seq


myList = [1, 2, 3, 4, 9, 10, 18, 19, 20, 21, 22, 23, 39, 40]
print(f"{find_longest_consecutive_seq(myList)}")