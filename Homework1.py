# Задача 1. Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.
# import math
# day = int(input('Введите день недели: '))
# if day == 1:
#     print('Понедельник')
# elif day == 2:
#     print('Вторник')
# elif day == 3:
#     print('Среда')
# elif day == 4:
#     print('Четверг')
# elif day == 5:
#     print('Пятница')
# elif day == 6:
#     print('Суббота')
# elif day == 7:
#     print('Воскресенье')
# else:
#     print('Нет такого дня')
#     Задача 2. Напишите программу, которая принимает на
# вход координаты двух точек и находит расстояние между
# ними в 2D пространстве
ax = float(input('Введите координаты по оси х: '))
ay = float(input('Введите координаты по оси y: '))
bx = float(input('Введите координаты по оси х: '))
by = float(input('Введите координаты по оси y: '))
import math
distance = math.sqrt((ax - ay)**2 + (bx - by)**2)
print(f'Расстояние между точками равно: {distance}')