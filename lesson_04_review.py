# Напишите программу, которая сравнивает пароль и его подтверждение.
# Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
"""
Write a program that compares the password and its confirmation.
If they match, then the program displays: "Accepted", otherwise: "Declined".
"""
# password = input()
# password_confirmation = input()
# if password == password_confirmation:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")
# ==========================================================================================
# Напишите программу, которая определяет, является число четным или нечетным.
"""
Write a program that determines if a number is even or odd.
"""
# num = int(input())
#
# if num % 2 == 0:
#     print("Четное")
# else:
#     print('Нечетное')

# ==========================================================================================
# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.

"""
Write a program that checks the following statement for a given four-digit number:
the sum of the first and last digits is equal to the difference (subtraction) between the second and third digits.
"""
# num = int(input())
# sum_1_and_2 = (num // 1000) + (num % 10)
# difference = ((num % 1000) // 100) - ((num % 100) // 10)
#
# if sum_1_and_2 == difference:
#     print('ДА')
# else:
#     print('НЕТ')

# ==========================================================================================
# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

"""
Write a program that determines whether a user is allowed to access an Internet resource or not.
The program should display the text "Access granted" if the age is at least 18, and "Access denied" otherwise.
"""
# age = int(input())
#
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# ==========================================================================================

# Напишите программу для вычисления и оценки индекса массы тела (ИМТ) человека.
# ИМТ человека рассчитывают по формуле:
#
# ИМТ = масса, (кг) / рост(м) * рост(м)
# Масса человека считается оптимальной, если его ИМТ находится между 18.5 и 25.
# Если ИМТ меньше 18.5, то считается, что человек весит ниже нормы.
# Если значение ИМТ больше 25, то считается, что человек весит больше нормы.
#
# Программа должна вывести "Оптимальная масса", если ИМТ находится между 18.5 и 25 (включительно).
# "Недостаточная масса", если ИМТ меньше 18.5 и "Избыточная масса", если значение ИМТ больше 25.

"""
Write a program to calculate and evaluate a person's body mass index (BMI).
BMI = mass, (kg) / height (m) * height (m)
The program should output "Optimal Weight" if the BMI is between 18.5 and 25 (inclusive). 
"Underweight" if BMI is less than 18.5 and "Overweight" if BMI is greater than 25.
"""
# weight = float(input())
# height = float(input())
# imt = weight / height ** 2
#
# if imt >= 18.5 and imt <= 25:
#     print("Оптимальная масса")
# elif imt > 25:
#     print("Избыточная масса")
# elif imt < 18:
#     print("Недостаточная масса")

# ==========================================================================================
# Напишите программу, которая принимает целое число x и определяет,
# принадлежит ли данное число указанному промежутку (-1, 17), не включая границы
"""
Write a program that takes an integer x and determines 
if the given number belongs to the specified range (-1, 17), not including the boundaries.
"""
# num = int(input())
# if num > -1 and num < 17:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# ==========================================================================================
# Напишите программу, которая принимает целое число xx и определяет,
# принадлежит ли данное число указанным промежуткам (-3, 7), включая границы

"""
Write a program that takes an integer x and determines 
# if the given number belongs to the specified range (∞, -3) and then (7, ∞), including the boundaries.
"""
# num = int(input())
# if num <= -3 or num >= 7:
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# ==========================================================================================
"""
Write a program that takes an integer x and determines 
# if the given number belongs to the specified range (-30, -2) and then (7, 25), 
left boundaries are not included and right ones are included.
"""
# num = int(input())
# if (num > -30 and num <= -2) or (num > 7 and num <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# ==========================================================================================
"""
Write a program that takes three positive numbers and determines if there exists a triangle with such sides.
длина любой стороны треугольника всегда меньше суммы длин двух его других сторон.
"""
# a = int(input())
# b = int(input())
# c = int(input())
#
# if (a < b + c) and (b < a + c) and (c < a + b):
#     print("YES")
# else:
#     print("NO")

# ==========================================================================================
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
"""
Write a program that takes three positive numbers and determines the type of triangle whose side lengths are equal to the given numbers.
The program should display text on the screen - a kind of triangle ("Equilateral", "Isosceles" or "Scales").
"""
# a = int(input())
# b = int(input())
# c = int(input())
#
# if a == b == c:
#     print("Равносторонний")
# elif a == b or b == c or a == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# ==========================================================================================
# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список, в котором содержатся только те числа, которые больше 5 по модулю.
"""
Write a program where the function more_than_five(lst) receives a list of integers. 
The result of the function should be a new list, which contains only those numbers that are greater than 5 modulo.
"""
# def more_than_five(lst):
#     new_lst = []
#     for number in lst:
#         if number > 4:
#             new_lst.append(number)
#     return new_lst
#
# print(more_than_five([-11, 14, -2, 90, 400, 0, -5]))
# print(more_than_five([-2, 2, 3, 4, 0, -1]))
# print(more_than_five([70, -900, 41, 0]))

# ==========================================================================================
# Write a program that determines the largest of the three given numbers
# Напишите программу, которая определяет наибольшее из трех введенных чисел
# num1 = float(input("Введи первое число: "))
# num2 = float(input("Введи второе число: "))
# num3 = float(input("Введи третье число: "))
#
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
#
# print("Наибольшее число из трех чисел", largest)