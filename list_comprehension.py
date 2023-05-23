"""
Collection of simple Python exercises about list comprehension
"""
#** 1) Square every number in a list.
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [n ** 2 for n in numbers]
# print(squared)

#** 2) Square even numbers in a list.
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [n ** 2 for n in numbers if n % 2 == 0]
# print(squared)

#** 3) Extract the initials from names.
# names = ['Falcon Punch', 'The Bug', 'Little Messi', 'Paul Nuts', 'Elvis Troll']
# initials = [name[0] + name.split()[1][0] for name in names]
# print(initials)

#** 4) Filter strings by length
# words = ['money', 'so', 'they', 'say', 'is', 'the', 'root', 'of', 'all', 'evil', 'today']
# small_words = [word for word in words if len(word) < 4]
# print(small_words)

#** 5) Create a list of tuples
# numbers = [1, 2, 3, 4, 5]
# list_of_tuples = [(n, n+1, n+2) for n in numbers]
# print(list_of_tuples)

#** 6) Flatten a nested list
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flattened_list = [num for sublist in nested_list for num in sublist]
# print(flattened_list)

#** 7) Convert a list of strings to uppercase
# words = ['hello', 'give', 'take', 'panda', 'water']
# words_to_upper = [word.upper() for word in words]
# print(words_to_upper)

#** 8) Generate a list of prime numbers

# First, let's code a function to check if a number is prime
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# numbers = range(0, 101)
# primes = [n for n in numbers if is_prime(n)]
# print(primes)

#** 9) Extract digits from a number
# number = 18491651
# digits = [int(digit) for digit in str(number)] # Convert number to str in order to be able to iterate (int object is not iterable), then we convert each digit back to int.
# print(digits)

#** 10) Generate a list of strings
# names = ['Polly', 'Brandy', 'Angie', 'Lola']
# greetings = [f"Hi, {name}" for name in names]
# print(greetings)

#** 11) Combine elements from two lists
# names = ['Polly', 'Brandy', 'Angie', 'Lola']
# ages = [18, 22, 20, 37]
# people = [(name, age) for name in names for age in ages]
# print(people)

#** 12) Generate list of multiples
# n = 5
# multiples = [i * n for i in range(1, 51)] # Remember: range(start(inclusive), stop(exclusive), step)
# print(multiples)
