from funcionesOyB import *

#Ejercicio en clase: Ordenamiento y búsqueda

#Ordenamiento de burbuja
print("\nOrdenamiento burbuja\n")

list = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada: ", list)
ordenamiento_burbuja(list)
print("Lista ordenada:", list)

#Ordenamiento por selección
print("\nOrdenamiento por selección\n")

list = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada: ", list)
ordenamiento_seleccion(list)
print("Lista ordenada:", list)

#Ordenamiento por inserción
print("\nOrdenamiento por inserción\n")

list = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada: ",list)
ordenamiento_insercion(list)
print("Lista ordenada:", list)

#Ordenamiento Merge sort
print("\nOrdenamiento por merge sort\n")

list = [64, 34, 25, 12, 22, 11, 90]
print("Lista desordenada: ",list)
merge_sort(list)
print("Lista ordenada:", list)