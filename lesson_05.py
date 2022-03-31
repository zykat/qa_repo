## FUNCTIONS ##
##тело функции
# def my_first_function():
#     print("Hello")
#
# ## вызов функции
# my_first_function()

# def inc_func(x):
#     ## increase x by 1
#     x = x + 1
#     print(x)
#
# inc_func(47)

# def sum_func(x, y):
#     print(x + y)
#
# sum_func(45, 23)

# def sum_func(x, y):
#     z = int((x + y) / 2)
#     text = f'Result of calculation: {z}'
#     print(text)
#
# a1 = 55
# b1 = 23
# sum_func(a1, b1)
#
# a2 = 345
# b2 = 45
# sum_func(a2, b2)
#
# a3 = 99
# b3 = -199
# sum_func(a3, b3)

## RETURN THE result OF Function
# def sum_func(x, y):
#       z = x + y
#       return z
# a1 = 14
# b1 = 16
# res = sum_func(a1, b1)
# print(f'Result is: {res}')

# def compare_func(x, y):
#       if x > y:
#             return True
#       else:
#             return False
#
# print(compare_func(5,5))

# def compare_func(x, y):
#       print(y)
#       if x > y:
#             return x
#       else:
#             return 0
#
# print(compare_func(70,5 + 75))
#
## GLOBAL - LOCAL VARIABLES
# x = 45 # global var
# def local_func():
#       x = 15 # local var
#       x += 5
#       print(f'local  x {x}')
# local_func()
# print(f'global x {x}')
#
# x = 45
# def local_func():
#       x = 15 # local var
#       x += 5
#       return x
# local_func()
# print(x + local_func())
#
####
# x = 45
# def local_func():
#       global x
#       r = 20 # local var
#       x += 5
#       print(x + r)
# local_func()
#
####
# pep8.org - python code standart
# wiki - don't repeat yourself
# wiki - KISS principle
# https://www.w3schools.com/python/default.asp
####
### HOMEWORK
####
# 1) Write a function to compare 2 numbers.
#     E.g.compare(2, 3)
# should return False otherwise should return True.
# def compare(x, y):
#     if x > y:
#         print("False")
#     else:
#         print("True")
# compare(2, 3)
#
# 2) Modify previous function to compare only positive numbers. In case
# of negative numbers it will return a print statement like: "Can compare only positive numbers!".
# def compare(x, y):
#     if x < 0 or y <0:
#         print("Can compare only positive numbers!")
#     elif x > y:
#         print("False")
#     else:
#         print("True")
# compare(20, 3)
#
# 3) Write a function to sum 2 numbers.
#     E.g.add(4, 5)
# should return 9 as a result.
# def sum_f(x, y):
#     print(x + y)
# sum_f(4, 5)
#
# 4) Write a function to subtract 2 numbers.
#     E.g.sub(4, 2)
# should return 2 as a result.
# def sub_f(x, y):
#     print(int(x / y))
# sub_f(4, 2)
#
# 5) Write a function that returns a type of input.
#     E.g.give_a_type("test")
# should return a print statement like: "string".
# z = ["name", "Joj", "game", "bnbn"]
# def type_f(x):
#     print(type(x))
# type_f(z)
#
# 6) Write a function that prints input vertically.
#     E.g.print_vertical("test me")
# should return:
# t
# e
# s
# t
#
# m
# e
#
d = "test me"
# def print_vertical(x):
#     for i in x:
#         print(i)
# print_vertical(d)
#
# 7) Write a function that concatenates 2 strings.
#     E.g.concat("abc", "123")
# should return a print statement like: "adc123".
#
# def concat(x, y):
#     print(str(x) + str(y))
#
# concat("abc", 123)