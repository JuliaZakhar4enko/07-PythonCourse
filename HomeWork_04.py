# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# import random
# list_1 = {random.randint(0,20) for _ in range (10)}
# print (list_1)
# list_2 = {random.randint(0,20) for _ in range (10)}
# print (list_2)

# i = list_1.intersection(list_2)
# print(*i)


# import random
# n = int(input("Введите количество элементов первого множества: "))
# list_1 = []
# for _ in range(n):
#     list_1.append(random.randint(0, 10))
# print(list_1)
# m = int(input("Введите количество элементов второго множества: "))
# list_2 = []
# for _ in range(m):
#     list_2.append(random.randint(0, 10))
# print(list_2)
# set_1 = set(list_1)
# set_2 = set(list_2)
# set_total = set_1.intersection(set_2)
# print(sorted(set_total))




# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
#  Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#  Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# import random
# n = int(input("Введите количество кустов: "))
# m = []
# for i in range(n):
#     m.append(random.randint(0, 10))
# print(m)
# sum = 0
# max_sum = 0
# i = 0
# while i < n:
#     if i < n-2:
#         sum = m[i]+m[i+1]+m[i+2]
#         if sum > max_sum:
#             max_sum = sum
#     if i == n-2:
#         sum = m[i]+m[i+1]+m[0]
#         if sum > max_sum:
#             max_sum = sum
#     if i == n-1:
#         sum = m[i]+m[0]+m[1]
#         if sum > max_sum:
#             max_sum = sum
#     i += 1
# print(max_sum)