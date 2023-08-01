# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1= 1, ak= ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию 

# fib1 = int(input("Введите номер числа Фибоначи: "))
# def fibonachi(fib1):
#     if fib1 == 1:
#         return 1
#     elif fib1 == 0:
#         return 0
#     else :
#         return fibonachi(fib1-1)+fibonachi(fib1-2)
# print(fibonachi(fib1))  

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random
# lenght_mass = int(input())
# random_mass = [random.randint(1,5) for _ in range(lenght_mass)]
# print(random_mass)
# i = 0
# while i< len(random_mass):
#     if random_mass[i]==4 or random_mass[i]==5:
#         random_mass[i]=1
#     i+=1
# print(random_mass)        


# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

# def is_simple(n):
#     for i in range(2, n//2):
#         if n%i == 0:
#             return False
#     return True
# print(is_simple(11))    








