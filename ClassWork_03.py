# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# import random
# my_list = [random.randint(0,10) for _ in range(20)]
# print(my_list)

# new_list = []
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)

# print(new_list)        
# print(len(new_list))

#или

# print(len(set(my_list)))  #перевели из списка во множество , все дубли удалились



# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# N = int(input("Введите N"))
# K = int(input("Введите K"))

# my_list = [i for i in range(N)]
# print(my_list)

# my_list_one = my_list[:K]
# my_list_two = my_list[K:]

# my_list_end = my_list_two + my_list_one
# print(my_list_end)


# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# print(my_dict)

# # unique = set()

# # for i in my_dict:
# #     unique.add(str(*i.values()))
# # print(unique)

# #или второй вариант:
# val = set()
# for d in my_dict:
#     for k,v in d.items():
#         val.add(v)

# print(val)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально

# array = [0, -1, 5, 2, 3]
# count = 0

# for i in range (1, len(array)):
#     if array [i] >array [i-1]: 
#         count +=1
# print(count)        