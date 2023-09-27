#Definicion de funciones

def most(a,b):
    if (a>b):
        return a
    else:
        return b
    
def least(a,b):
    if(a<b):
        return a
    else:
        return b

#Programa principal

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

print(most(x-3, least(x+2, y-5)))

#El programa estaba utilizando dentro de las funciones las variables globales, lo cual, aparte de ser una mala práctica, no están siendo bien utilizadas ya que los parámetros de la función son a y b por lo tanto no sufren las modificaciones dentro de la funcion.