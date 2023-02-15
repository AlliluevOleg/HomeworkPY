import random
import matplotlib.pyplot as plt
import numpy

# задача 1. Постройте график функции𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно.
def zd1():
    x_list = []
    y_list = []

    for x in range(-10, 11):
        y = 5 * x * x + 10 * x - 30
        x_list.append(x)
        y_list.append(y)


    plt.axhline(y = 0, color = 'r')
    plt.plot(y_list)
    plt.show()    
zd1()
# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов,
# отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.
def zd2():
    house = 15
    area_of_houses = [random.randint(100, 300) for _ in range(house)]
    price_houses = [random.randint(3000000, 20000000) for _ in range(house)]
    mean_result = [round(price_houses[i] / area_of_houses[i]) for i in range(len(price_houses))]
    print(mean_result)
    plt.axhline(y = 50000, color = 'b')
    houses = ['д1','д2','д3','д4','д5','д6','д7','д8','д9','д10','д11','д12','д13','д14','д15']
    plt.bar(houses, mean_result )
    plt.show()
zd2()
