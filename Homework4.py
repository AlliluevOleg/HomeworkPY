from math import pi
# # Напишите программу, которая составит список простых множителей числа N.
# def zadacha1():
#     num = int(input("Введите число: "))
#     i = 2  
#     lst = []
#     old = num
#     while i <= num:
#         if num % i == 0:
#             lst.append(i)
#             num //= i
#             i = 2
#         else:
#             i += 1
#     print(f"Простые множители числа {old} приведены в списке: {lst}")
# zadacha1()

def zadacha3():
    d = int(input("Введите число для заданной точности числа Пи:\n"))
    print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
zadacha3()