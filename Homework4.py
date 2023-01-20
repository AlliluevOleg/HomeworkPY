from math import pi
# Напишите программу, которая составит список простых множителей числа N.
def zadacha1():
    num = int(input("Введите число: "))
    i = 2  
    lst = []
    old = num
    while i <= num:
        if num % i == 0:
            lst.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Простые множители числа {old} приведены в списке: {lst}")
zadacha1()
# Задача 2. В первой строке файла находится информация об ассортименте мороженного, 
# во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
def zadacha2():
    data = open ('icecream.txt,',mode='r', encoding='utf-8')
    file = data.readlines()
    data.close
    magazin = set(file[0].removesuffix('\n').split(', '))
    sklad = set(file[1].removesuffix('\n').split(', '))
    res = magazin.difference(sklad)
    print(f'Закончилось мороженное {res}')

#     Задача 3. Выведите число π с заданной точностью. Точность выводится
# в виде десятичной дроби
def zadacha3():
    d = int(input("Введите число для заданной точности числа Пи: "))
    print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
zadacha3()