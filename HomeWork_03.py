# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# import random
# my_list = [1,2,3,3,4,5]
# print(my_list)
# k = 3

# count = 0
# for item in my_list:
#     if item == k:
#         count += 1
# print(count)



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# # 5
# # 1 2 3 4 5
# # 6
# # -> 5

list_1 = [1, 2, 3, 4, 5]
k = 6

d_min = sum(list_1)
for i in list_1:
    if abs(k-i) < d_min:
        d_min = abs(k-i)
        i_min = i
print(i_min)


# import random
# n = int(input("Введите количество элементов в массиве: "))
# m = []
# for _ in range(n):
#     m.append(random.randint(0, 5))
# print(m)
# x = int(input("Введите число X от 1 до 5: "))
# d_min = sum(m)
# for i in m:
#     if abs(x-i) < d_min:
#         d_min = abs(x-i)
#         i_min = i
# print(f'Самый близкий по величине элемент к числу {x} --> {i_min}')





# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
# Ввод:
# ноутбук
# Вывод:
# 12


my_dict = {1: 'A,E,I,O,U,L,N,S,T,R,А,В,Е,И,Н,О,Р,С,Т',
           2: 'D,G,Д,К,Л,М,П,У',
           3: 'B,C,M,P,Б,Г,Ё,Ь,Я',
           4: 'F,H,V,W,Y,Й,Ы',
           5: 'K,Ж,З,Х,Ц,Ч',
           8: 'J,X,Ш,Э,Ю',
           10: 'Q,Z,Ф,Щ,Ъ'}
k = "ноутбук"
#k = list(input('Input word: '))
count = 0
for elem in k:
    for key, value in my_dict.items():
        if elem.upper() in value:
            count += key
print(f'Word value: {count}')
