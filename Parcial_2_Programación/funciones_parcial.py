#Funciones parcial 2 programación

#Función para rellenar los strings con la secuencia de ADN
def string_Filling(counter_):
    print("\n\tIntroduzca la", (counter_),"° secuencia de caracteres de la base nitrogenada de ADN de este humano:")
    dna_String = (input("\n\t")).upper()
    return dna_String

#Función para validar la longitud de cada string (6 caracteres)
def string_Long(dna_String):
    if (len(dna_String) != 6):
        return " "
    else:
        return dna_String

#Función para validar los caracteres de cada string (A,T,G,C)
def string_Chars(dna_String):
    for i in range(6):
        if ((dna_String[i] == "A") or (dna_String[i] == "C") or (dna_String[i] == "G") or (dna_String[i] == "T")):
            continue
        else:
            return " "
    return dna_String

#Función para determinar la mutación de ADN
def is_Mutant(dna):
    #Contador de secuencias. Si hay 2 o más, la función retornará TRUE dando por encontrado el gen mutante
    sequence_Counter = 0
    #Caso HORIZONTAL
    #Se toma la primera fila y se comparan los elementos de la posicion 0 a la 3, si son iguales se suma al contador
    #Si no se comparan los de la posicion 1 a la 4,si son iguales se suma al contador y lo mismo con la posición 2 a la 5
    #Se repite este proceso para las 5 filas restantes
    for i in range(6):
        for j in range(3):
            if (((dna[i])[0+j:4+j] == "AAAA") or ((dna[i])[0+j:4+j] == "TTTT") or ((dna[i])[0+j:4+j] == "CCCC") or ((dna[i])[0+j:4+j] == "GGGG")):
                sequence_Counter += 1
    
    #Caso VERTICAL
    #Se toman los strings 1 a 4 y se comparan los primeros elementos de cada string. Si son iguales se suma un elemento al contador
    #Si no, se repite el proceso con los strings 2 a 5, y si tampoco, se vuelve a repetir con los strings 3 a 6
    #Luego comparamos el siguiente elemento de cada string de la misma manera ya sí hasta el elemento final
    for i in range(3):
        for j in range(6):
            if ((dna[0+i])[j] == (dna[1+i])[j] == (dna[2+i])[j] == (dna[3+i])[j]):
                sequence_Counter += 1

    #Caso DIAGONAL
    #Dividido en dos partes: Una para las líneas diagonales en sentido descendente y otra en sentido ascendente
    for i in range(3):
        for j in range(3):
            #Diagonales DESCENDENTES: se toma el 1er elemento del 1er string y lo compara con el 2do el. del 2do string, el 3er el del 3er string y el 4to el. del 4to string
            #Si son iguales suma uno al contador de secuencias
            #Si no se repite el proceso tomando el 2do del 1ero string, 3ro del 2do y asi sucesivamente buscando 4 igualdades
            #Se repite este proceso para los 3 primeros strings
            if ((dna[0+i])[0+j] == (dna[1+i])[1+j] == (dna[2+i])[2+j] == (dna[3+i])[3+j]):
                sequence_Counter += 1
            #Diagonales ASCENDENTES: Funciona de manera similar, pero tomando los 3 últimos strings
            elif ((dna[5-i])[0+j] == (dna[4-i])[1+j] == (dna[3-i])[2+j] == (dna[2-i])[3+j]): 
                sequence_Counter += 1
    
    if (sequence_Counter >= 2):
        return True
    else:
        return False