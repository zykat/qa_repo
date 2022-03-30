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
####
#
