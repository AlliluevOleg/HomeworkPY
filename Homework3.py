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
# let = input('Введите первую букву названия фрукта: ')
# data = open('fruits.txt', mode='r', encoding='utf-8')
# text = data.readlines()
# data.close
# first_liter = ''
# count = 0
# for let in text:
#     if let == text[0]:
#         first_liter = text
#         print(first_liter)
        
        
# phrase = input(  )
# dictionary = {
#             'Привет': 'Здравствуйте',
#             'Как тебя зовут': 'Олег'
# }
# if phrase == dictionary[phrase]:
#     print(dictionary['Привет'])

