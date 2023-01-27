import random
# Задача 1:  Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины.
def Zd1():
    n = input('Введите число: ')
    nn = int(n+n)
    nnn = int(n+n+n)
    n = int(n)
    result = n+nn+nnn
    print(f'Числа {n} + {nn} + {nnn} = {result}')
# Zd1()    
# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число.
# Напишите программу, которая определяет,
# есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
def Zd2():
    list = [random.randint(1, 10) for _ in range(1, 10)]
    print(list)
    number_input = int(input('Введите трехзначное число: '))
    res = ''
    for el in list:
        res += str(el)
    print(res)
    if str(number_input) in res:
        print('Есть совпадение')
    else:
        print("совпадений не найдено")
Zd2()

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11
def check_numbers(x,y):
    min_numbers = min(x,y)
    divider = 1
    for el in range(2, min_numbers+1):
        if x % el ==0 and y % el == 0:
            divider = el
            break
    return divider == 1 

def Zd3():
    for y in range (1, 12):
        for x in range(1, y):
            if check_numbers(x, y):
                print(f'{x}/{y}', end=' ')
        print()
Zd3()