from funciones import *

#Ejercicio 1

dni = input("Ingrese su número de dni: ")

validation = dni_Validation(dni)

if (validation == True):
    print("dni válido")
else:
    print("dni inválido")

#Ejercicio 2

string = input("Escriba algo: ")
list = string.split()
long = int(len(list))

print("La última palabra tiene" , long_String(list, long), "letras")

#Ejercicio 3

name = " "

name_Numbers = input("Ingrese CANTIDAD de nombres del socio: ")

name = (input("Ingrese su nombre completo (nombres y un apellido): ")).split()
dni = input("Ingrese su número de DNI: ")
validation = dni_Validation(dni)

if (validation != True):
    while (validation != True):
        print("dni inválido")
        dni = input("Ingrese su número de DNI: ")
        validation = dni_Validation(dni)

print("dni válido")

letters_Lastname = find_Lastname(name)

dni_Digits = dni[0:3]

print(f"Su ID es: {name[0]}{letters_Lastname}{dni_Digits}")

#Ejercicio 4

number1 = int(input("Ingrese un número distinto de cero: "))
number2 = int(input("Ingrese otro número distinto de cero: "))

if ((number1 % number2) == 0):
    print("Un número es múltiplo del otro")
elif ((number2 % number1) == 0):
    print("Un número es múltiplo del otro")
else:
    print("no son múltiplos entre sí")

multiple = multiplo(number1, number2)

if (multiple == True):
    print(number1, "es múltiplo de", number2)
else:
    print(number1, "no es múltiplo de", number2)

#Ejercicio 5

cant_Days = int(input("Cantidad de días: "))

for i in range(cant_Days):
    print("Temperatura máxima del día" , (i+1) , ": ", end="")
    max_Temp = int(input())
   
    print("Temperatura mínima del día" , (i+1) , ": ", end="")
    min_Temp = int(input())

    media = media_Temp(max_Temp, min_Temp)

    print("Temperatura media del día ", (i+1), ": ",media, "°C")

#Ejercicio 6

space = " "
string = input("Escriba algo: ")

space = spaced_String(string)

print("")

#Ejercicio 7

cant_Numbers = int(input("Ingrese CANTIDAD de números: "))
list = []

for i in range(cant_Numbers):
        num = int(input("Ingrese un número: "))
        list += [num]

max_Number = the_Max(list)
min_Number = the_Min(list)

print("Máximo:", max_Number)
print("Mínimo:", min_Number)

#Ejercicio 8

rad = float(input("Ingrese el radio: "))

area = calculate_Area(rad)
per = calculate_Per(rad)

print("Área: ", area)
print("Perímetro: ", per)

#Ejercicio 9

print("Log In")

bool = True
trys = 0

while (bool == True):
    trys += 1
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    check_Log = login(username, password, trys)

    if (check_Log == True):
        print("Acceso permitido")
        break
    else:
        print("Acceso denegado. Intentos: ", trys)

    if (trys == 3):
        print("Límite de intentos")
        break

#Ejercicio 10

cost = {1:200, 2:300, 3:150, 4:450, 5:800}
percentage = {1:15, 2:10, 3:20, 4:25, 5:50}
final_Cost = {}

for i in range(len(cost)):
    print(f"Precio original del producto n°{i+1}: ${cost[i+1]}")
    print(f"Descuento: %{percentage[i+1]}")
    print("\t")

final_Cost = supermarket(cost, percentage)

for i in range(len(cost)): 
    print(f"Precio final {i+1}: $",final_Cost[i+1])

#Ejercicio 11

list = []
modified_List = funcion2(funcion1)
print("Lista modificada: ", modified_List)

#Ejercicio 12

string = input("Escriba algo: ")

dictionary = modify_Phrase(string)

for i in range(len(dictionary)):
    print(f"{i+1}° palabra y su longitud: {dictionary[i]}")
print("\t")

#Ejercicio 13

vx = float(input("Ingrese la magnitud del vector en la dirección X: "))
vy = float(input("Ingrese la magnitud del vector en la dirección Y: "))
vz = float(input("Ingrese la magnitud del vector en la dirección Z: "))

final_Result = calculate_Vector(vx,vy,vz)

print("El módulo del vector V es: ", final_Result)

#Ejercicio 14

num = int(input("Ingrese un número entero: "))

result = cousin(num)

if (result == True):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")

#Ejercicio 15

cant_Num = int(input("Ingrese CANTIDAD de números: "))

for i in range (cant_Num):
    print((i+1), "° número: ", end="")
    num = int(input(" "))
    result = factorizador(num)
    while (num > 0):
        if (num > 1):
            print(num, "x ", end="")
        else:
            print(num, "=", end=" ")
        num -=1
    print(result)

#Ejercicio 16

print("ingresar un numero entero")
number=int(input())
print("ingresa un digito para ver cuantas veces aparece en el numero anteriormente ingresado")
dig=int(input())

print("La cantidad de veces que aparece el digito",dig,"en el numero",number,"es de:",busdig(dig,number),"veces")

#Ejercicio 17

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