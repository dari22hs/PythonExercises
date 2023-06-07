"""
Collection of simple Python exercises using lambda functions.
Syntax:
#? -> lambda arguments: expression

## arguments --> refers to the input parameters of the function
## expression -> is the single expression that gets evaluated and returned as the result of the function
"""
#** 1) Add two numbers
# add = lambda x, y: x + y
# result = add(9, 11)
# print(result)

#** 2) Filter even numbers from a list
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_nums)

#** 3) Sort a list of tuples based on the second element
# points = [(1, 5), (3, 2), (2, 8), (4, 3)]
# sorted_points = sorted(points, key=lambda x: x[1])
# print(sorted_points)

#** 4) Square a list of numbers
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

#** 5) Convert a list of strings to uppercase
# words = ["joke by me", "mouse", "hamster", "play"]
# uppercase_words = list(map(lambda x: x.upper(), words))
# print(uppercase_words)

#** 6) Find the maximum value in a list of tuples
# ages = [('Dewey', 12), ('Jody', 22), ('George', 42)]
# max_ages = max(ages, key=lambda x: x[1])
# print(max_ages)

#** 7) Count the number of characters in a list of strings
# words = ["hi", "good", "morning", "user"]
# char_count = list(map(lambda x: len(x), words))
# print(char_count)

#** 8) Find palindromes in a list of strings
# strings = ["hello", "radar", "user", "level"]
# palindromes = list(filter(lambda x: x == x[::-1], strings))
# print(palindromes)

#** 9) Combine first and last names from a list of dictionaries
# names = [{'first': 'John', 'last': 'Striker'}, {'first': 'Thomas', 'last': 'Hope'}, {'first': 'Florence', 'last': 'Cash'}, {'first': 'Seth', 'last': 'Garner'}]
# full_names = list(map(lambda x: x['first'] + ' ' + x['last'], names))
# print(full_names)

#** 10) Filter prime numbers from a list
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
prime_numbers = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)), numbers))
print(prime_numbers)
