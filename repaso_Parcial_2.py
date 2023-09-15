#Ejercitación de repaso

#Ejercicio 1

phrase = str(input("Escriba una frase/palabras: "))

if (len(phrase) == 4):
    print(phrase,"!")
else:
    print(phrase,"?")

#Ejercicio 2

import random

list = ["enzo", "mac", "udolfo", "gualter", "naccio"]

choice_List = random.choice(list)

print("")
print("Grand Theft Auto VI")
print("")
print(f"La palabra tiene {len(choice_List)} letras")
print("")
print("Intento número 1")

for i in range(len(choice_List)):
    print("Adivine la ",i+1,"° letra de la palabra")
    letter = str(input(""))
    try_ = i+1
    if (letter == choice_List[i]):
        print("Correcto!")
    elif (letter != choice_List[i]):
        while(letter != choice_List[i]):
            print("Incorrecto.",try_ + 1,"° intento")
            print("Adivine la ",i+1,"° letra de la palabra")
            letter = str(input(""))

            try_ += 1

            if (letter == choice_List[i]):
                print("Correcto!")

print("")
print(f"Excelente! La palabra era {choice_List}")
print(f"Utilizaste {try_} intentos")
print("")
print("mission passed!")
print("    Respect +")

#Ejercicio 3

text_Line = str(input("Ingrese su frase favorita: "))
text_Line = text_Line.lower()
word_Counter = 0

for i in range(len(text_Line)):
    word = text_Line[i]
    if (word == " ")  :
        word_Counter += 1
    elif (i == len(text_Line) - 1): 
        word_Counter += 1
    
print(f"La frase ingresada tiene {word_Counter} palabras")

#Ejercicio 4

bool = True

while bool == True:

    salary = float(input("Ingrese el sueldo del empleado: "))

    attendace = str(input("¿El empleado asisitió el mes completo? "))
    attendace = attendace.lower()

    if ((attendace != "si") and (attendace != "no")):
        while ((attendace != "si") and (attendace != "no")):
            print("Responda si o no")
            attendace = str(input("¿El empleado asisitió el mes completo? "))
            attendace = attendace.lower()

    if (attendace == "si"):
        extra_Hours = int(input("¿Cuantas horas trabajó los domingos? "))
        if ((extra_Hours >= 3) and (extra_Hours <= 5)):
            salary = (salary * 0.03) + salary
        elif ((extra_Hours >= 6) and (extra_Hours <= 10)):
            salary = (salary * 0.1) + salary

    if (attendace == "no"):
        extra_Hours = int(input("¿Cuantas horas trabajó los domingos? "))
        if ((extra_Hours >= 3) and (extra_Hours <= 10)):
            salary = (salary * 0.02) + salary

    print(f"El sueldo final del empleado es de ${salary}")
    print("")
    repeat = str(input("¿Desea repetir el procedimiento para otro empleado? "))
    repeat = repeat.lower()
    if ((repeat != "si") and (repeat != "no")):
        while ((repeat != "si") and (repeat != "no")):
            print("Responda si o no")
            repeat = str(input("¿Desea repetir el procedimiento para otro empleado? "))
            repeat = repeat.lower()

    if (repeat == "si"):
        continue
    else:
        break

#Ejercicio 5

number_1 = float(input("Ingrese un primer número: "))
number_2 = float(input("Ingrese un segundo número: "))

if (number_1 == number_2):
    result = number_1 * number_2
    print(f"{number_1} x {number_2} = {result}")
elif (number_1 > number_2):
    result = number_1 - number_2
    print(f"{number_1} - {number_2} = {result}")
else:
    result = number_1 + number_2
    print(f"{number_1} + {number_2} = {result}")

#Ejercicio 6

bool = True

while (bool == True):

    age = int(input("Ingrese su edad: "))
    if ((age < 0) or (age > 125)):
        while ((age < 0) or (age > 125)):
            print("Ingrese una edad válida")
            age = int(input("Ingrese su edad: "))

    antiquity = int(input("Ingrese sus años de antigüedad: "))
    if ((antiquity < 0) or (antiquity + 18 > age)):
        while ((antiquity < 0) or (antiquity + 18 > age)):
            print("Ingrese una antigüedad válida")
            antiquity = int(input("Ingrese sus años de antigüedad: "))

    if ((age >= 60) and (antiquity < 25)):
        retirement = "jubilación por edad"
    elif ((age < 60) and (antiquity >= 25)):
        retirement = "jubilación por antigüedad joven"
    elif ((age >= 60) and (antiquity >= 25)):
        retirement = "jubilación por antigüedad adulta"
    else:
        retirement = "no hay una jubilación para su condición"

    print(f"Usted queda adscrito a: {retirement}")

    repeat = str(input("¿Desea repetir el procedimiento para otro jubilado? "))
    repeat = repeat.lower()
    if ((repeat != "si") and (repeat != "no")):
        while ((repeat != "si") and (repeat != "no")):
            print("Responda si o no")
            repeat = str(input("¿Desea repetir el procedimiento para otro jubilado? "))
            repeat = repeat.lower()

    if (repeat == "si"):
        continue
    else:
        print("Gracias por confiar en ANSES")
        break

#Ejercicio 7

bool = True

while (bool == True):

    salary = float(input("Ingrese el salario del trabajador: "))
    if (salary < 0):
        while (salary < 0):
            print("No explote a sus trabajadores")
            salary = float(input("Ingrese el salario del trabajador: "))

    month = str(input("¿El trabajador lleva menos de un año? "))
    month = month.lower()
    if ((month != "si") and (month != "no")):
        while ((month != "si") and (month != "no")):
            print("Responda si o no")
            month = str(input("¿El trabajador lleva menos de un año? "))
            month = month.lower()

    if (month == "si"):
        utility = salary * 0.05
        salary = utility + salary
    else:
        antiquity = float(input("Ingrese sus años de antigüedad: "))
    
        if (antiquity < 0):
            while (antiquity < 0):
                print("Ingrese una antigüedad válida")
                antiquity = float(input("Ingrese sus años de antigüedad: ")) 
    
        if ((antiquity >= 1) and (antiquity < 2)):
            utility = salary * 0.07
            salary = utility + salary
        elif ((antiquity >= 2) and (antiquity < 5)):
            utility = salary * 0.1
            salary = utility + salary
        elif ((antiquity >= 5) and (antiquity < 10)):
            utility = salary * 0.15
            salary = utility + salary
        elif (antiquity >= 10):
            utility = salary * 0.2
            salary = utility + salary

    print(f"La utilidad que recibirá el trabajador es de ${utility}, y su sueldo final será de ${salary}")

    repeat = str(input("¿Desea repetir el procedimiento para otro trabajador? "))
    repeat = repeat.lower()
    if ((repeat != "si") and (repeat != "no")):
        while ((repeat != "si") and (repeat != "no")):
            print("Responda si o no")
            repeat = str(input("¿Desea repetir el procedimiento para otro trabajador? "))
            repeat = repeat.lower()

    if (repeat == "si"):
        continue
    else:
        print("Hasta luego!")
        break