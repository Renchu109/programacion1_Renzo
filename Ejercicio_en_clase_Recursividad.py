import random

#Ejercicios en clase recursión

#Ejercicio 1

#Escribir una función que simule el siguiente experimento: Se tiene una rata en una
#jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
#probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
#minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
#La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
#quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
#La función debe devolver el tiempo que tarda la rata en salir de la jaula.

def recursivity(time_):
    path = random.randint(1, 3)  
    if (path == 3):
        return 7 + (time_)
    elif(path == 2):
        return 5 + recursivity(time_)
    else:
        return 3 + recursivity(time_)

time = 0

final_Time = recursivity(time)

print("\nTiempo final: ", final_Time)

#Ejercicio 2

#Escribir una consigna apropiada para la siguiente función. Asumir que n es un número entero.

#Consigna: Escribir una función que reciba como parámetro un número entero y lo retorne de atrás hacia adelante. Utilizar recursividad
def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    
    return s[-1] + f(s[:-1])

n = 123456

reves = f(n)

print(n, " al reves: ", reves)