a = 1
b = 3
c = 4
# #print(a, b, c, sep='*', end='***')
#
# v = ('|' + ' ' *10 + '|')
#
# print("-" * 12)
# print(v, v, v, sep='\n')
# print("-" * 12)


## Напишите программу, которая выведет приветствие, где имя вводится с клавиатуры.
# name = input('What is your name?')
# print(type(name))
# print(f'Hello, {name}')

# Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
# Первое число вводит пользователь, остальные числа вычисляются в программе.

# x = int(input("Input your number: "))
# y = x + 1
# z = y + 1
# print(x, '\n', y, '\n', z, sep='')

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму.
# Kаждое число записано в отдельной строке.

# a = int(input("Put first value: "))
# b = int(input("Put second value: "))
# c = int(input("Put second value: "))
#
# print(a + b + c)

# =======
# x, y, z = int(input()), int(input()), int(input())
# print(x + y + z)

# =======
#print(int(input("Put first value: ")) + int(input("Put second value: ")) )

# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# На вход программе подается одно целое число – длина ребра.
# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3,  S = 6a^2

# a = int(input("Введите ребро: "))
# print(f'Площадь: {a * 6 ** 2}')
# print(f'Объем: {a ** 3}')

# Напишите программу вычисления значения функции
# f(a, \, b) = 3(a + b)^3 + 275b^2 - 127a - 41 по введеным целым значениям aa и bb.

# a = int(input('a = '))
# b = int(input('b = '))
# f = 3 * (a + b)**3 + 275 * b ** 2 - 127 * a - 41
# print(f)

# Напишите программу, которая считывает целое число, после чего на экран
# выводится следующее и предыдущее целое число с пояснительным текстом.

# a = int(input('Number = '))
# b = (a - 1)
# c = (a + 1)
# print(f'Previous number: {b}')
# print(f'Next number: {c}')

# ====

# x = int(input())
# print(f"Следующее за числом {x} число: {x + 1}")
# print("Следующее за числом", x, "число:", x + 1)
# print(f"Для числа {x} предыдущее число: {x - 1}")

# Напишите программу, которая считает стоимость трех компьютеров,
# состоящих из монитора, системного блока, клавиатуры и мыши.
# На вход программе подаётся четыре целых числа, каждое на отдельной строке.
# В первой строке — стоимость монитора,
# во второй строке — стоимость системного блока, в третьей строке — стоимость
# клавиатуры и в четвертой строке — стоимость мыши.

# m = int(input("Монитор: "))
# sb = int(input("Системный блок: "))
# k = int(input("Клавиатура: "))
# mx = int(input("Mouse: "))
# print(m+sb+mx+k)

# Напишите программу, в которой вычисляется сумма,
# разность и произведение двух целых чисел, введенных с клавиатуры.
# a = int(input())
# b = int(input())
# print(f"{a} + {b} =", a + b)
# print(f"{a} - {b} =", a - b)
# print(f"{a} * {b} =", a * b)
# print(f"{a} / {b} =", a / b)

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.

# cm = int(input())
# m = cm // 100
# print(m)

#Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения
# Вселенной # по #щелчку пальцев. При этом если население Вселенной является нечетным числом,
# то титан проявит милосердие и округлит #количество выживших в большую сторону.
# Помогите Мстителям подсчитать количество выживших.
p = int(input("Population: "))
survivors = p// 2 + p % 2
print(survivors)
