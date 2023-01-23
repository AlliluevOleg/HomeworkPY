import random
# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. Используйте для решения лямбда-функцию
def zadacha1():
    len = 10
    fun = lambda el: el > 5
    numbers = [random.randint(1, 10) for _ in range(len)]
    print(numbers)
    result = list(filter(fun, numbers))
    print(result)
zadacha1()    
