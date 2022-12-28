# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
def zadacha1():
    number = int(input('Введите число '))
    fact = []
    value = 1
    for i in range(1, number+1):
        fact.append(value)
        value *= i + 1
    print(fact)
zadacha1()    
# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def zadacha2():
   for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x and y) or z == 1:
                print(x, y, z)
zadacha2()
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def zadacha3():
    from collections import Counter
    phrase = ['o, n, e']
    text = 'onetwonine'
    c = Counter(text)
    c.most_common(3)
    print(c)
zadacha3()
# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def zadacha4 ():
    xs = [2, 3, -3, -2, -1, 0, 1]
    xs = xs[-2:] + xs[:-2] 
    print(xs)
zadacha4()