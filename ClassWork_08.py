# 1.напечатать сторку в одну линию  C:\WINDOWS\System32\drivers\etc\nst
# print(r'C:\WINDOWS\System32\drivers\etc\nst')


# a = [4, 3, -10, 1, 7, 12]
#     [4, -10, 12, 3, 1, 7]

# a.sort(key=lambda x: x%2)

# print(a)


# 4. Напишите программу, которая подсчитает и выведет сумму квадратов всех двузначных чисел, делящихся на 9.
# При решении задачи используйте комбинацию функций filter, map, sum.

# Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат.
#  lst = sum([x**2 for x in range(10, 100) if x%9==0])
# print(lst)

# nums_2digits = [x for x in range(10,100)]
# nums = list(filter(lambda x: x % 9 == 0, nums_2digits))
# res = list(map(lambda x: x*x, nums))
# print(sum(res))