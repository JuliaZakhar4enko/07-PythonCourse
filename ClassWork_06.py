# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# 4 15 43 1 15 1 (каждое число вводится с новой строки)


# import random
# list1 =[random.randint(0,10) for _ in range(10)]
# print(list1)
# list2 =[random.randint(0,10) for _ in range(10)]
# print(list2)
# list_temp = []
# for i in list1:
#     if i not in list2:
#         list_temp.append(i)

# print(list_temp)


# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

# import random
# length_mass_1= int(input("Input length of list: "))
# random_mass_1 =[random.randint(0,10) for _ in range(length_mass_1)]
# count = 0
# for i in range(-1, length_mass_1 -1):
#     if random_mass_1[i-1] < random_mass_1[i] and random_mass_1[i+1]<random_mass_1[i]:
#         count +=1
# print(random_mass_1)
# print(count)      


# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# import random
# length_mass_1= int(input("Input length of list: "))
# random_mass_1 =[random.randint(0,10) for _ in range(length_mass_1)]
# count = 0
# for i in random_mass_1:
#     if random_mass_1.count(i)>1:
#         count += 1

# print(count //2)      
# print(random_mass_1)  










