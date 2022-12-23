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