"""
Collection of quizzes taken from the Internet
"""
#* 1) What is the output?
## A) SyntaxError
## B) bark bark!
##    None
## C) bark bark!
## D) None of the above
# class dog: 
#     ...


# @(lambda f:setattr(dog, "on_leash", f))
# def walk():
#     print("bark bark!")


# print(dog.on_leash())

#* 2) What is the output?
## A) [1, 2, 3]
## B) [100, 2, 3]
## C) [100, 100, 100]
## D) [2, 3]
# x = [1, 2, 3]
# y = x
# y[0] = 100
# print(x)

#* 3) What is the output?
## A) Py.py = 7 Cy.py = 3.14 Vy.py = 7
## B) Py.py = 7 Cy.py = 1 Vy.py = 3.14
## C) None of the above
## D) Py.py = 3.14 Cy.py = 7 Vy.py = 1
# class Py:
#     py = 1
    
    
# class Cy(Py):
#     ...


# class Vy(Py):
#     ...


# Cy.py = 3.14
# Py.py = 7
# print(f"{Py.py = } {Cy.py = } {Vy.py = }")

#* 4) What is the output?
## A) True 
## B) False
## C) None
## D) "Lion"
# def func():
#     a, *b, c = ["Cat", "Dog", "Tiger", "Lion"]
#     item = b
#     return "Lion" in [item] or None


# print(func())

#* 5) What is the output?
# my_string = "Python"
# result = my_string[::2] + my_string[1::2]
# print(result)

#* 6) What is the output?
## A) True
## B) Empty
## C) Not Empty
## D) False
# a = [""]
# b = 2
# c = ""
# print("Empty" if c is a or c == a else not "Not Empty")

#* 7) What is the output?
## A) SyntaxError
## B) True
## C) False
## D) None
# print(False == False in [False])

#* 8) What is the output?
## A) [] ['']
## B) [''] ['']
## C) [] []
## D) [''] []
# s = '\n'
# print(s.split(), s.splitlines())