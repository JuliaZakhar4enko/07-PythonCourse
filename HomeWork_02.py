# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# import random
# coins = [random.randint(0,1) for _ in range (9)]
# print (coins)

# count_0 = 0
# count_1 = 0
# for coin in coins:
#     if coin ==0:
#         count_0 +=1
        
#     else:
#         count_1 += 1
# if count_0 > count_1:
#     print(" Перевернуть единички")    
# else:
#     print(" Перевернуть нолики")        



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# sum = int(input("Введите сумму двух чисел: "))
# mult = int(input("Введите произведение двух чисел: "))
# print (sum, mult)
# print ( round (mult / (sum - 2)))
# print ( round (sum - (mult/(sum - 2))))

#или второй вариант:
# x=int(input("Введите сумму двух чисел: "))
# y = int(input("Введите произведение двух чисел: "))
# for i in range (x):
#     for j in range (y):
#         if x == i + j and y == i*j:
#             print(i,j)



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# number = int (input("Введите предел: "))
# i =1
# while i< number:
#     print (i,  end='  ')
#     i*=2




