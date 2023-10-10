from funciones import *

#Ejercicio 16

maxx=0
while(True):
    print("ingresar numero primo")
    number=int(input())
    iss=prime(number)
    if(iss>maxx):
        maxx==iss
    if (iss==False):
        break
    else:
        
        dig=input("ingresar un digito para ver cuantas veces aparece en el numero ingresado: ")
        print("la suma de sus digitos es:",primadd(number))
        print("La cantidad de veces q sale el digito",dig," es de:",busdig(dig, number))
        print("El factorial del mayor numero ingresado que es",maxx,"es de:",factorial(maxx))