"""
In Python, setattr() is a built-in function that allows you to set the value of an attribute on an object using its name as a string. It's a powerful tool that enables you to dynamically modify attributes of objects at runtime. The function has the following syntax:
#? setattr(object, name, value)

## object: The object on which you want to set the attribute.
## name: A string representing the name of the attribute you want to set.
## value: The value you want to assign to the attribute
"""
#* 1)
class MyClass:
    def __init__(self):
        self.my_attribute = None

obj = MyClass()

# Setting the 'my_attribute' attribute to the value 42 using setattr()
setattr(obj, 'my_attribute', 42)

# Accessing the attribute directly to verify the value
print(obj.my_attribute)  # Output: 42
