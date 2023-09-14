#TP4_Break_Continue

#Exercise 1

x = 0

while(x < 30):
    if (x == 15):
        print("La ejeución del ciclo se rompió con el valor",x, "de x")
        x += 1
        break
    elif (x == 4 or x == 6 or x == 10):
        print("El valor", x, "de x fue salteado")
        x += 1
        continue
    else:
        print("El valor del ciclo es:", x)
        x += 1

#Exercise 2

bool = "true"

while (bool == "true"):
    line = str(input("Ingrese palabras/frase o no ingrese nada para cerrar el ciclo: "))
    if (line == ""):
        break
    print(line.upper())

#Exercise 3

bool = "true"
reserv = 0

while (bool == "true"):
    action = str(input("Ingrese la acción que desea realizar (formato: D xxx / R xxx) o no ingrese nada para terminar el ciclo: "))
    action = action.upper()
    
    if (action == ""):
        break

    sub_action = action[0 : 1]
    value = int(action[2 : len(action)])

    if (sub_action == "D"):
        reserv += value   
    elif (sub_action == "R"):
        reserv -= value
           
print("Reserva en el banco: $", reserv)

#Exercise 4

bool = "true"
cousins = 0
divisors = 0

print("Ingrese números mayores que 1:")
while (bool == "true"):
    number = int(input("--> "))

    if (number < 0):
        print("Mayores que 1")
        continue
    elif (number == 0):
        print("Fin de ciclo")
        break

    for i in range(1, number + 1):
        if ((number % i) == 0):
            divisors += 1

    if (divisors == 2):
        cousins += 1

    divisors = 0

print("Se ingresaron", cousins, "números primos")

#Exercise 5

year_1 = int(input("Ingrese un primer año: "))
year_2 = int(input("Ingrese un segundo año: "))

minor = year_1
major = year_2
if (year_2 < year_1):
    minor = year_2
    major = year_1

for i in range(minor, major + 1, 1):
    if ((i % 4 == 0) and ((i % 100 != 0) or (i % 400 == 0)) and (i % 10 == 0)):
        print(i)

#Exercise 6

for i in range(0, 21, 1):
    if (i % 2 != 0):
        continue
    else:
        print(i)

#Exercise 7

list = [0,1,2,3,4,5,6,7,8,9]

number = int(input("Número a buscar (del 0 al 9): "))

for i in range(0, 10, 1):
    if (i == number):
        print("Número encontrado: ",i)
        break
    else:
        print("Número no encontrado: ",i)

#Exercise 8

bool = "true"

print("--Bienvenidos al restaurante MadMax 5--")

print("MENU DEL DIA")
print("Menú 1 - Lunes")
print("Menú 2 - martes")
print("Menú 3 - miercoles")
print("Menú 4 - jueves")
print("Menú 5 - viernes")

while (bool == "true"):
    option = int(input("Ingrese una opción para ver el menú de ese día o ingrese cero para salir: "))
    if (option == 1):
        print("Menú 1: milanesa de ternera con guarnición")
    elif (option == 2):  
        print("Menú 2: pastel de papa")  
    elif (option == 3):  
        print("Menú 3: ravioles de ricota y verdura con salasa a elección")
    elif (option == 4):  
        print("Menú 4: pata muslo al horno con guarnición")
    elif (option == 5):  
        print("Menú 5: tarta de verduras asadas con mozzarella")
    elif ((option < 0) or (option > 5)):  
        print("Opción inválida")
        continue    
    elif (option == 0):
        print("Gracias por ver el menú")
        break