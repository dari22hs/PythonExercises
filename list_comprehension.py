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
# names = ['Michael', 'Bug', 'Messi', 'Paul', 'Elvis']
# initials = [name[0] for name in names]
# print(initials)

#** 4) Filter strings by length
# words = ['money', 'so', 'they', 'say', 'is', 'the', 'root', 'of', 'all', 'evil', 'today']
# small_words = [word for word in words if len(word) < 4]
# print(small_words)

#** 5) Create a list of tuples
# numbers = [1, 2, 3, 4, 5]
# list_of_tuples = [(n, n+1, n+2) for n in numbers]
# print(list_of_tuples)