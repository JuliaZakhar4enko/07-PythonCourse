# import random
# data = [random.randint(0,20) for _ in range (10)]
# print (data)
# res = list()

# for i in data:
#     if i%2 == 0:
#        res.append((i, i**2))

# print(res)

# def select(f, col):
#     return [f(x) for x in col]   

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1,2,3,4,5,6,7,8,]
# res = select(int,data)
# print(res)
# res = where(lambda x: x%2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)



# Функция map

# data = "23 45 67 87 98"

# data = list(map(int,data.split()))
# print(data)

#Функция filter

# data = [15, 43, 45, 60, 165]
# data = list(filter(lambda x: x%10 == 5, data))
# print(data)

# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# values = [1, 23, 42, "asdfg"]
# trasformation = lambda x: x       
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print("ok")
# else:
#  print("fail")
       

#        Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# # используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

def find_farthest_orbit(orb):
    new_orb= list(filter(lambda x: x[0]!= x[1], orb))
    # for cort in orb:
    #     if cort[0]==cort[1]:
    #         new_orb.append(cort)
    return max(new_orb, key=lambda x: x[0]*x[1])        

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))



