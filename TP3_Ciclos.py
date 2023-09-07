#Trabajo práctico n° 3: ciclos

#Ejercicio 1

palabra = str(input("Ingrese una palabra: "))
for i in range(10):
    print(palabra)

#Ejercicio 2

edad = int(input("Hola usuario. Ingrese su edad: "))

for i in range(edad):
    i = i+1
    print(i)

#Ejercicio 3

nro = int(input("Ingrese un número entero positivo: "))

for i in range(nro):
    if (i % 2 != 0):
        if (i == nro - 1):
            print(i, end="")        
        else:
            print(i, ", ", end="")
    i = i + 1 
print("")

#Ejercicio 4

nro = int(input("Ingrese un número: "))

while nro >= 0:
    if (nro != 0):
        print(nro, ", ", end="")
    else:
        print(nro, end="")
    nro = nro - 1
print("")

#Ejercicio 5

inversion = int(input("Ingrese la cantidad de dinero a invertir: "))
interes = float(input("Ingrese el interés anual: %"))
anios = int(input("¿Por cuántos años? "))

for i in range(anios):
    total = inversion + ((inversion * interes) / 100)
    print(f"Año {i + 1}: $",total)
    inversion = total

#Ejercicio 6
height = int(input("Ingrese la altura: "))

for i in range(height):
    while (i >= 0):
        print("*", end="")
        i -= 1
    print("")

#Ejercicio 7

for i in range(10):
    print("TABLA DEL ", i+1)
    for j in range(10):
        print(i+1, " x ", j+1, " = ", ((i+1) * (j+1)))

#Ejercicio 8

height = int(input("Ingrese la altura: "))

for i in range(1, height + 1):
    for j in range(2 * i - 1, 0, -2):
        print(j, end=" ")
    print()

#Ejercicio 9

var = "contraseña"
intento = str(input("Ingrese la contraseña: "))

while (intento != var):
    intento = str(input("Vuelva a ingresar la contraseña: "))

print("La contraseña ingresada es correcta")

#Ejercicio 10

nro = int(input("Ingrese un número entero: "))
cont_divisores = 0

for i in range(nro):
    if (nro % (i + 1) == 0):
        cont_divisores = cont_divisores + 1

print(f"Divisible por {cont_divisores} valores")
#Un número es primo sólo si es divisible por dos números: 1 y sí mismo
if (cont_divisores > 2):
    print(f"{nro} no es un número primo")
else:
    print(f"{nro} es un número primo")

#Ejercicio 11

palabra = input("Ingrese una palabra: ")
largo1 = len(palabra)
largo2 = largo1
alreves = ""

for i in range(largo1):
    largo2 = largo2 - 1
    letra = palabra[largo2]
    alreves = alreves + letra
print(alreves)

#Ejercicio 12 

phrase = str(input("Escriba una frase: "))
letter = str(input("Escriba una letra: "))
counter = 0

for i in range(len(phrase)):
    if (letra == phrase[i]):
        counter = counter + 1

print(counter)

#Ejercicio 13 

val = "oh yeah"

while (val == "oh yeah"):
    phrase = input("Escribi algo rey: ")
    if (phrase == "salir"):
        val = "Oh no"
        print("Saliendo rey")

#Ejercicio 14 

number_1 = int(input("Ingrese un primer nùmero: "))
number_2 = int(input("Ingrese un segundo nùmero: "))

bigger = number_1
smaller = number_2

if (number_2 > bigger):
    bigger = number_2
    smaller = number_1

while (smaller < bigger):
    if (smaller % 2 != 0):
        print(f"{smaller} es impar")
    else:
        print(f"{smaller} es par")
    smaller = smaller + 1

# Ejercicio 15


number1 = int(input("Ingrese un número entero positivo: "))
counter = 1
if (number1 == 0 or number1 < 0):
    print("Debe ingresar un número mayor a 0.")
else:
    print(f"Los siguientes números son divisores de {number1}:")
    while counter <= number1:
        if (number1 % counter == 0):  
            print(counter)
            counter = counter + 1
        else:
            counter = counter + 1



#Ejercicio 16 
numbers = int(input("¿Cuàntos nùmeros va a introducir? "))

counter = 0

for i in range(numbers):
    number = int(input(f"Ingrese el {i+1}º  nùmero: "))
    if (number < 0):
        counter += 1

print(f"Introdujo {counter} nùmeros negativos")


#Ejercicio 17 
phrase = input("Ingrese una frase: ")
used1 = 0
used2 = 0
used3 = 0
used4 = 0
used5 = 0
vowels = ""
large = len(phrase)
print("Las siguientes vocales están en su frase: ")
for i in range(large):
    if (phrase[i] == "a" and used1 == 0):
        vowels = vowels + phrase[i] + ", "
        used1 = used1 + 1
    elif (phrase[i] == "e" and used2 == 0):
        vowels = vowels + phrase[i] + ", "
        used2 = used2 + 1
    elif (phrase[i] == "i" and used3 == 0):
        vowels = vowels + phrase[i] + ", "
        used3 = used3 + 1
    elif (phrase[i] == "o" and used4 == 0):
        vowels = vowels + phrase[i] + ", "
        used4 = used4 + 1
    elif (phrase[i] == "u" and used5 == 0):
        vowels = vowels + phrase[i] + ", "
        used5 = used5 + 1
print(vowels)

#Ejercicio 18 
last_number_1 = 0
last_number_2 = 1

print("0, 1", end="" + ", ")

for i in range(10):
    fibo = last_number_1 + last_number_2
    if (i != 9):
        print(fibo, end="" + ", ")
    else:
        print(fibo, end="")
    last_number_1 = last_number_2
    last_number_2 = fibo

#Ejercicio 19
piggy_bank = int(input("¿Cuánto dinero quieres ahorrar?: $"))
money2 = 0
while money2 < piggy_bank:
    money1 = int(input("¿Cuánto dinero guardarás?: $"))
    if (money1 < 0):
        print("No se admiten números negativos.")
    money2 = money2 + money1
print(f"¡Lograste tu objetivo! Ahorraste ${money2}")

#Ejercicio 20 
val = "oh yeah"
add = 0

while (val == "oh yeah"):
    number = int(input("Ingrese un nùmero: "))
    if (number == 0):
        val = "oh no"
    else:
        add += number 

print("Sumatoria: ",add)

#Ejercicio 21 

val = "oh yeah"
bigger = 0

while (val == "oh yeah"):
    number = int(input("Ingrese un nùmero positivo: "))
    if (number == 0):
        val = "oh no"
    elif (number > bigger):
        bigger = number

print("Mayor: ",bigger)

#Ejercicio 22

number = int(0)
sumatory = int(0)

while(number != -1):
    number = int(input("Ingrese un número para sumar sus dígitos: "))
    if (number < 0 and number != -1):
            number *= -1
    while (number > 1):
        sumatory += number % 10
        number /= 10
    print(int(sumatory))
    sumatory = 0
        
#Ejercicio 23, 24 

cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
cost = int(cost)
totalcost = 0
while cost != 0:
    if cost < 0:
        cost = input("Por favor, ingrese un monto positivo ")
        cost = int(cost)
        continue
    totalcost = totalcost + cost
    cost = input("Ingrese el monto de la compra o ingrese 0 para terminar ")
    cost = int(cost)
   
if totalcost > 1000 :
    discount = totalcost/10
    totalcost = totalcost - discount
   
print("Su precio final es: $", totalcost)


#Ejercicio 25 

number = int(input("Ingrese un número: "))
fact = number

for i in range(number, 1, -1):
    print(i, "x ", end="")
    fact *= (i - 1)
print("1 =", fact, end="")