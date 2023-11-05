from funciones_parcial import *

#Parcial 2 Programación

print("\n-------------------------------------------------------DETECCIÓN DE MUTANTES-------------------------------------------------------\n\n")

print("Buen día Magneto, mediante este programa usted podrá detectar si un humano es mutante o no mediante su ADN")
print("Usted deberá ingresar las 6 secuencias de 6 bases nitrogenadas del ADN del humano en cuestión, representadas por las letras A, T, C, G")
print("Se detectará gen mutante si hay más de una secuencia de cuatro bases iguales de forma horizontal, vertical o diagonal.\n")

human_Counter = 1

#Ciclo para repetir el programa las veces requeridas
while (bool):

    print("\n",human_Counter,"° Humano\n")
    #Matriz a rellenar con las secuencias, las cuales serán 6 y estarán determinadas por el contador
    dna_List = []
    counter = 1

    #Ciclo para rellenar 6 secuencias
    while (bool):

        print("\n", counter,"° Secuencia\n")

        #Función para rellenar cada secuencia
        dna_Sequence = string_Filling(counter)

        #Función para validar que sean 6 caracteres
        dna_Long = string_Long(dna_Sequence)

        #Función para validar que sean caracteres válidos
        dna_Chars = string_Chars(dna_Long)

        #Ciclo anidado para determinar que la secuencia rellenada sea válida
        if ((dna_Long == " ") or (dna_Chars == " ")):
            while ((dna_Long == " ") or (dna_Chars == " ")):
                print("-------------------------------------------------------------------------------------------------------------------------------------")
                print("\n\tErrores detectados.")
                print("\tRecuerde Magneto que debe la longitud de cada secuencia es de 6 caracteres y los caracteres válidos son A,C,G,T")
                print("\tVuelva a rellenar la ",(counter),"° secuencia: \n")
                print("-------------------------------------------------------------------------------------------------------------------------------------")
                dna_Sequence = string_Filling(counter)
                dna_Long = string_Long(dna_Sequence)
                dna_Chars = string_Chars(dna_Long)
        
        #Agregar la secuencia a la lista para formar la matriz
        dna_List.append(dna_Sequence)

        #Condición para rellenar solamente 6 secuencias
        if (len(dna_List) == 6):
            print("\n",counter,"° Secuencia de ADN rellenada correctamente")
            break

        counter += 1

    #Muestra de la matriz
    print("\n")
    print("------------------Matriz de secuencia de ADN------------------\n")
    for row in dna_List:
        for element in row:
            print("\t", end="")
            print(" ",element, end="")
        print(" ")
    print("\n--------------------------------------------------------------")

    #Funcion is_Mutant(dna) para determinar si el humano tiene ADN mutante o no
    mutation = is_Mutant(dna_List)

    #Mensaje a mostrar de acuerdo a los resultados obtenidos
    if (mutation):
        print("\n\tResultado: positivo. Este humano presenta ADN mutante\n")
    else:
        print("\n\tResultado: negativo. Este humano no presenta ADN mutante\n")

    #Condición de repetición
    print("\n\tSr. Magneto ¿Desea comprobar el ADN de otro humano?")
    answer = input("\n\t").lower()
    if ((answer != "si") and (answer != "no")):
        while ((answer != "si") and (answer != "no")):
            print("\n\tPor favor responda si o no")
            answer = input("\n\t").lower()

    if (answer == "si"):
        human_Counter += 1
        continue
    else:
        break

print("\n--------------------------------------------------------------")
print("\nPrograma finalizado. Suerte con su búsqueda")
print("\n--------------------------------------------------------------\n\n")