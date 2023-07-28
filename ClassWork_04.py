# 1

my_dict ={ 1:'one', 2:"two", 3:"three"}
# my_list = ["three", "four", "five"]

# for i,j in my_dict.items():
#     if j in my_list:
#         print(i)
#         break
# else: 
#     print (False)   

#если надо найти ключ по значению используй
# print (my_dict.get(1, "Такого ключа нет"))

#добавляем ключ в словарь:
# print (my_dict)

# my_dict[4] = 'four'
# print(my_dict)

#Добавить в словарь
# print(my_dict)
# my_dict.setdefault(5, 'five')
# my_dict.setdefault(3, 'five')
# print(my_dict)


# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# str_1 = 'a a a b c a a d c d d'.split()
# print(str)

# some_string = input ("Введите строку: ")

# cnt_dict = {}
# for ch in some_string:
#     if ch in cnt_dict:
#         cnt_dict[ch] +=1
#     else :
#         cnt_dict[ch] = 0
#     print(ch if cnt_dict[ch] < 1 else f'{ch}_{cnt_dict[ch]}', end=' ')    
           

# Задача №27. Общее обсуждение
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов или символами конца строки.Определите,
# сколько различных слов содержится в этом тексте.
# Input:She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells. 
# Output: 19

# from string import punctuation
# text = '''She sells sea shells on the sea shore;The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore,I'm sure that the shells are sea shore shells.'''

# # text = text.split()
# # # sign = ["." "," ":" ";" "'"]
# # # for i in range(len(sign)):
# # #     text = text.replace(sign[i]," ")
# # print(len(set(text)))

# #second versia


# for i in punctuation.replace("'", ' '):
#     text = text.replace(i, ' ')

# print(text.lower())   

# print(len(set(text.lower().split()))) 


# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Петя:1111
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n) 


# Ваня:111
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# n = int(input("Введите число:  "))
# max_number = n
# while n != 0:
#      n = int(input())
#      if max_number < n:
#           max_number = n
# print(max_number)