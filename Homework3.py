# Задача 1. Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.
def zadacha1():
    n = int(input('Введите длину ряда: '))
    f1 = 0
    f2 = 1
    data = open('fib.txt', mode='w', encoding='utf-8')
    for i in range(n):
        f1, f2 = f2, f1 + f2
        data.write(str(f1) + '\n')
        data.close
        print(f2, end=' ')
   
zadacha1()
# Задача 2. В файле находятся названия фруктов.
# Выведите все фрукты, названия которых начинаются на
# заданную букву.
def zadacha2():
    let = input('Введите первую букву названия фрукта: ')
    data = open('fruits.txt', encoding='utf-8')
    Fruits_lst = data.readlines()[0].split(' ')
    data.close
    for fruit in Fruits_lst:
        if fruit[0] == let:
            print(fruit)
zadacha2()        
#  Задача 3. Создайте скрипт бота, который находит ответы
# на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза
# ему неизвестна, он выводит соответствующую фразу.       
def zadacha3():
    dictionary = {
            'привет': 'Здравствуйте',
            'как тебя зовут?': 'Олегсей'
}
    dia = True
    while dia:
        phrase = input('Я ')
        if phrase in dictionary.keys():
            print(f'Bot: {dictionary[phrase]}')
        else:
            print(f'Bot: не понимать')
        if phrase == 'пока':
            dia = False
zadacha3()

