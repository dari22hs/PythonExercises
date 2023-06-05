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
celsius_temps = [20, 21, 22, 23, 24, 25]
fahrenheit_temps = list(map(lambda c: (9/5) * c +32, celsius_temps))
print(fahrenheit_temps)