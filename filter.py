"""
Examples of filter function.

The filter() function in Python is a built-in function that allows you to create an iterator from an iterable (such as a list, tuple, or set) by applying a given filter function to each element of the iterable. It returns an iterator that contains only the elements from the original iterable for which the filter function returns True.

The filter() function works by applying the filter function to each element of the iterable. If the filter function returns True for an element, that element is included in the resulting iterator. If the filter function returns False, the element is excluded.

Syntax:
#? filter(function, iterable)

## function -> filter function that takes one argument and returns a boolean value (True or False)
## iterable -> sequence, collection, or iterator that you want to apply the filter function to
"""
#** 1) Even numbers
# def is_even(n):
#     return n % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(is_even, numbers))
# print(even_numbers)

#** 2) Positive numbers
# def is_positive(n):
#     return n > 0

# numbers = [-12, -8, -2, 0, 1, 4, 7, 12]
# positive_numbers = list(filter(is_positive, numbers))
# print(positive_numbers)

#** 3) Strings longer than 5 characters
# def is_long_string(s):
#     return len(s) > 5

# words = ["hello", "run", "good", "old", "dog", "watermelon", "chronical"]
# long_words = list(filter(is_long_string, words))
# print(long_words)
