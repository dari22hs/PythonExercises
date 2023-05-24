"""
Compilation of enumerate exercises.

The enumerate() function in Python is used to iterate over a sequence (such as a list, tuple, or string) while simultaneously obtaining the index and the corresponding element at each iteration. It provides a way to access both the index and the value of an item within a loop.

Syntax:
enumerate(sequence)

"""
#** 1) Enumerate list of names
# names = ['John', 'Paul', 'George', 'Ringo']

# for index, name in enumerate(names):
#     print(f"Person {index+1}: {name}")
    
#** 2) Enumerate a string
# message = "Welcome to the family, son."

# for index, char in enumerate(message):
#     print(f"Character at index {index}: {char}")

#** 3) Create a dictionary with enumerated elements
# cities = ["New York", "Los Angeles", "Barcelona", "Paris"]

# cities_dict = {index+1: city for index, city in enumerate(cities)}
# print(cities_dict)

#** 4) Enumerate with a starting index
# fruits = ["apple", "banana", "watermelon", "orange", "pineapple"]

# for index, fruit in enumerate(fruits, start=1):
#     print(f"Index: {index} -> Fruit: {fruit}")

#** 5)  Enumerate with condition
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]
for index, num in enumerate(numbers):
    if num % 10 == 0:
        print(f"Number {num} is at index {index} and is divisible by 10.")

