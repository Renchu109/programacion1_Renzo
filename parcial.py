#Ejercicio Parcial

bool = True

print("")
name = input("Hola Usuario! Dime como debo llamarte: ")
print("")

while (bool == True):

    
    print(f"De acuerdo {name}, elige una opción para jugar")
    print("1. Juego de números")
    print("2. Juego de palabras")

    choice = input("")
    if ((choice != "1") and (choice != "2")):
        while ((choice != "1") and (choice != "2")):
            print(f"{name}, debes ingresar el número del juego que desees")
            choice = input("")

    if (choice == "1"):
        print(f"{name}, has elegido el camino de los números")
        print("")
        pair_Major = 0
        pair_Number = 0
        odd_Number = 0
        while (bool == True):
            print(f"Ingresa un número entero, {name} o ingresa 0 si te rindes:")
            number = int(input(""))

            if (number == 0):
                print(f"Ciclo terminado, {name}")
                break

            if (number % 2 == 0):
                pair_Number += 1
                if (number > pair_Major):  
                    pair_Major = number
            elif(number % 2 != 0):
                odd_Number += 1

        print(f"pares: {pair_Number}")
        print(f"impares: {odd_Number}")
        total_Numbers = pair_Number + odd_Number
        porecentage = int((odd_Number * 100) / total_Numbers)  
        print(f"El mayor número par es: {pair_Major}")
        print(f"El porcentaje de impares es: {porecentage}%")

    elif (choice == "2"):

        print(f"{name}, has elegido el camino de las palabras")
        print("")
        print(f"Ingresa tu frase favorita, {name}")
        phrase = input("")
        phrase = phrase.lower()
        vocal_Counter = 0
        vocal_Counter_a = 0
        vocal_Counter_e = 0
        vocal_Counter_i = 0
        vocal_Counter_o = 0
        vocal_Counter_u = 0

        for i in range(len(phrase)):

            if ((phrase[i] == "a") or (phrase[i] == "e") or (phrase[i] == "i") or (phrase[i] == "o") or (phrase[i] == "u")):
                vocal_Counter += 1

            if (phrase[i] == "a"):
                vocal_Counter_a += 1
            elif (phrase[i] == "e"):
                vocal_Counter_e += 1
            elif (phrase[i] == "i"):
                vocal_Counter_i += 1
            elif (phrase[i] == "o"):
                vocal_Counter_o += 1
            elif (phrase[i] == "u"):
                vocal_Counter_u += 1    


        print(f"El total de vocales es {vocal_Counter}, de las cuales:")
        print(f"{vocal_Counter_a} son A's")
        print(f"{vocal_Counter_e} son E's")
        print(f"{vocal_Counter_i} son I's")
        print(f"{vocal_Counter_o} son O's")
        print(f"{vocal_Counter_u} son U's")


    repeat = input("¿Deseas volver a jugar? ")
    repeat = repeat.lower()
    if ((repeat != "si") and (repeat != "no")):
        while ((repeat != "si") and (repeat != "no")):
            print(f"{name}, responde si o no")
            repeat = input("¿Deseas volver a jugar? ")
            repeat = repeat.lower()

    if (repeat == "si"):
        continue
    else:
        print(f"Hasta luego {name}!")
        break