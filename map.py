"""
Examples of map function

The map() function in Python is a built-in function that applies a given function to each item of an iterable (such as a list, tuple, or set) and returns an iterator that yields the results.

The map() function applies the provided function to each item of the iterable and returns an iterator that yields the transformed values. The returned iterator can be converted into other data structures such as a list, tuple, or set using the list(), tuple(), or set() functions, respectively.

Syntax:
#? map(function, iterable)

## function -> function to be applied to each item of the iterable. This function can be a built-in function or a custom-defined function.
## iterable -> iterable object, such as a list, tuple, or set, whose items are to be passed through the function.
"""
#** 1) Square numbers
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x ** 2, numbers))
# print(squared_numbers)

#** 2) Convert temperatures from °C to °F
# celsius_temps = [20, 21, 22, 23, 24, 25]
# fahrenheit_temps = list(map(lambda c: (9/5) * c + 32, celsius_temps))
# print(fahrenheit_temps)

#** 3) Convert a list of strings to uppercase
# strings = ["henlo", "going", "find", "searching", "sweet"]
# uppercase_strings = list(map(str.upper, strings))
# print(uppercase_strings)

#** 4) Calculate the length of each word in a sentence
# sentence = "I'm going to learn Python"
# word_lengths = list(map(len, sentence.split()))
# print(word_lengths)

#** 5) Double each number in a list
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(doubled_numbers)

#** 6) Extract the first character in each string in a list
# names = ['Michael', 'Irma', 'Karen', 'Enzo']
# first_chars = list(map(lambda name: name[0], names))
# print(first_chars)
