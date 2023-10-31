import random
#Funciones TP6: Variables dimensionadas

#Ejercicio 1

def number_List(list_, bool_):
    while (bool_ == True):
        number = int(input("Número: "))
        list_.append(number)
        if (number == 0):
            print("Programa finalizado")
            break
    
    return list_

#Ejercicio 2

def delete_Ocu(list_,num):
    counter = list_.count(num)
    if (counter != 0):
        for i in range(len(list_)):
            if (num == list_[i]):
                del list_[i]
                break

    return list_

#Ejercicio 3

def sum_Elements(list_,sum):
    for i in range(len(list_)):
        sum += list_[i]
    
    return sum

#Ejercicio 4

def minor_Elements(list_, num):
    list_2 = []
    for i in range(len(list_)):
        if (list_[i] < num):
            list_2.append(list_[i])

    return list_2

#Ejercicio 10

def randomizer():
    x = random.randint(0,9)
    return x