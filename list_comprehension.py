"""
Collection of simple Python exercises about list comprehension
"""
#** 1) Write a Python program to square every number in a list.
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [n ** 2 for n in numbers]
# print(squared)

#** 2) Write a Python program to square even numbers in a list.
# numbers = [1, 2, 3, 4, 5, 6]
# squared = [n ** 2 for n in numbers if n % 2 == 0]
# print(squared)

#** 3) Write a Python program to extract the initials from names.
names = ['Michael Crack', 'The Bug', 'Little Messi', 'Paul Nuts', 'Elvis Joel']
initials = [name[0] for name in names]
print(initials)