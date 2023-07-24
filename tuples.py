"""
Tuples exercises
"""
#* Example 1: Unpacking with * for multiple variables
first, *middle, last = (10, 20, 30, 40, 50)
print(first)     # Output: 10
print(middle)    # Output: [20, 30, 40]
print(last)      # Output: 50

#* Example 2: Unpacking strings with *
first, *rest = "hello"
print(first)     # Output: 'h'
print(rest)      # Output: ['e', 'l', 'l', 'o']

#* Example 3: Unpacking with nested tuples and *
nested_tuple = (1, (2, 3), 4, (5, 6))
a, (b, c), *d = nested_tuple
print(a)         # Output: 1
print(b, c)      # Output: 2 3
print(d)         # Output: [4, (5, 6)]

#* Example 4: Ignoring elements with *
first, *_ = (100, 200, 300, 400)
print(first)     # Output: 100

#* Example 5: Using * in function parameter for variable-length arguments (args)
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4, 5)
# Output:
# 1
# 2
# 3
# 4
# 5
