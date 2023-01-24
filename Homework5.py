import random
# Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
#  Используйте для решения лямбда-функцию
def zadacha1():
    len = 10
    fun = lambda el: el > 5
    numbers = [random.randint(1, 10) for _ in range(len)]
    print(numbers)
    result = list(filter(fun, numbers))
    print(result)
zadacha1()    
# # Дан список случайных чисел. Создайте список, в который попадают числа, 
# # описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя
def zadacha2():
    nums = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
    print(nums)
    index = random.randint(0,len(nums)-1)
    res = [nums[index]]
    while index < len(nums):
        index = random.randint(index, len(nums))
        if index!= len(nums) and nums[index] > res[-1]:
            res.append(nums[index])
    print(res)
zadacha2()
# # задача3: Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# # Удалите все повторяющиеся элементы.
def zadacha3():
    len = 10
    list = [random.randint(1, 10) for _ in range(len)]
    print(f'Данный список {list}')
    list1 = []
    count = 0
    for i in list:
        if i not in list1:
            count +=1
            list1.append(i)
    print(f' Уникальные значения {list1}')
    print(f' Количество уникальных {count}')
          
zadacha3()
