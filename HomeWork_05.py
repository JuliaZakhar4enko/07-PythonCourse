# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 


# 
# def degree(a, b):
#     if b == 0:
#         return 1
#     return degree(a, b-1)*a


# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print(f'{a}^{b} --> {degree(a, b)}')


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:
# sum(2, 2)
# # 4

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a-1, b+1)


# a = int(input("Введите число a: "))
# b = int(input("Введите число b: "))
# print(f'{a}+{b} --> {sum(a, b)}')