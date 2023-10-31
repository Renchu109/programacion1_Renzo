from Funciones_6 import *

#TP6: Variables dimensionadas

#Ejercicio 1: 
#Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

list = []
bool = True

print("\nEjercicio 1\n")

print("Ingrese números")

full_List = number_List(list, bool)

print("Lista llena: ", full_List)

#Ejercicio 2 
#A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
#eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

print("\nEjercicio 2\n")
print("Ingrese un número: ", end="")
number = int(input())

if (number in list):
    print(number,"está en la lista")
else:
    print(number,"no está en la lista")

print("Lista original: ",list)

final_List = delete_Ocu(list, number)

print("Lista modificada: ",final_List)

#Ejercicio 3
#Imprimir la sumatoria de todos los números de la lista.

print("\nEjercicio 3\n")
sum = 0
sum_Result = sum_Elements(list, sum)

print("Lista: ", list)
print("Suma de elementos: ", sum_Result)

#Ejercicio 4	
#Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
#que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

print("\nEjercicio 4\n")
number = int(input("Ingrese un número: "))

print("Lista original: ", list)
final_List = minor_Elements(list, number)
print("Lista creada: ", final_List)

#Ejercicio 5 
#Generar e imprimir una nueva lista que contenga como elementos a tuplas, 
#cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 

print("\nEjercicio 5\n")

list = [4,8,7,5,9,6,5]

conteo = {}
for elemento in list:
    if elemento in conteo:
        conteo[elemento] += 1
    else:
        conteo[elemento] = 1

list2 = [(elemento, conteo[elemento]) for elemento in conteo]

print("Lista: ", list)
print("Nueva lista tuplada: ", list2)  

#Ejercicio 6
#Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. 
#A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
#a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
#b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
#c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

pr_List = []
sc_List = []
bool = True

print("\nNombres de alumnos de primaria")
print("Para finalizar, ingrese x\n")
while bool:
    pr_Name = input("Nombre: ")
    if (pr_Name == "x"):
        print("\nRegistrados todos los nombres de alumnos de primaria")
        break
    else:
        pr_List.append(pr_Name)
        continue

print("\nNombres de alumnos de secundaria")
print("Para finalizar, ingrese x\n")
while bool:
    sc_Name = input("Nombre: ")
    if (sc_Name == "x"):
        print("\nRegistrados todos los nombres de alumnos de secundaria")
        break
    else:
        sc_List.append(sc_Name)
        continue

pr_set = set(pr_List)
sc_set = set(sc_List)

print("\nNombres de los alumnos de primaria\n")
for name in pr_set:
    print(name)

print("\nNombres de los alumnos de secundaria\n")
for name in sc_set:
    print(name)

print("\nNombres que se repiten entre alumnos de primaria y secundaria\n")

repeat = []

for pr_Name in pr_List:
     for sc_Name in sc_List:   
        if (pr_Name == sc_Name):
            repeat.append(pr_Name)

set_repeat = set(repeat)  
for repeat_name in set_repeat:
    print(repeat_name)          

print("\nNombres que no se repiten entre alumnos de primaria y secundaria\n")

not_repeat_names = pr_set - sc_set
for name in not_repeat_names:
    print(name)

#Ejercicio 7
#Escribir un programa que procese strings ingresados por el usuario. 
#La lectura finaliza cuando se hayan procesado 50 strings. 
#Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados.

# Inicializar un diccionario para almacenar las ocurrencias de cada carácter
ocurrencias = {}

# Contador de strings procesados
strings_procesados = 0

while strings_procesados < 50:
    entrada = input("Ingresa un string (o 'x' para finalizar): ")
    
    # Verificar si el usuario desea finalizar la entrada
    if entrada == 'x':
        break
    
    # Contabilizar las ocurrencias de cada carácter en el string
    for caracter in entrada:
        if caracter in ocurrencias:
            ocurrencias[caracter] += 1
        else:
            ocurrencias[caracter] = 1
    
    strings_procesados += 1

# Imprimir las ocurrencias de cada carácter
print("\nOcurrencias de caracteres en todos los strings ingresados:")
for caracter, cantidad in ocurrencias.items():
    print(f"'{caracter}': {cantidad}")

#Ejercicio 8
#Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, 
#participaron en un campeonato de fútbol con modalidad todos contra todos.
#Escriba un programa que:
#Lea el cuadro de goles en un arreglo de dos dimensiones.
#Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#Determine la cantidad de puntos obtenidos por cada equipo.
 
