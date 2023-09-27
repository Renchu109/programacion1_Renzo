"""Funciones"""

#Funcion para buscar una palabra al azar
def randomize_Word(x):
    return random.choice(x)

#Funcion para mostrar la palabra
def showing_Word(word, guessed_Letters):
    show_The_Word = ""
    for letter in word:
        if (letter in guessed_Letters):
            show_The_Word += letter
        else:
            show_The_Word += "_"

    return show_The_Word

#Funcion para repetir el juego
def repeat_Game(do_it):
    do_it = input("¿Deseas volver a jugar? ").lower()
    if ((do_it != "si") and (do_it != "no")):
        while ((do_it != "si") and (do_it != "no")):
            print("Responde si o no")
            do_it = input("¿Deseas volver a jugar? ").lower()

    if (do_it == "si"):
        print("Cargando nuevo juego...")
        print("")
        play_Ahorcado()
    else:
        print("Garcias por jugar!")

    return do_it

#Funcion principal del juego

def play_Ahorcado():

    random_Word = randomize_Word(word_List)

    trys = 6
    guessed_Letters = []
    bool = True

    print("AHORCADO")
    print("")
    print(f"Inicias con {trys} vidas")

    while bool == True:
        
        showed_Word = showing_Word(random_Word, guessed_Letters)

        if (showed_Word == random_Word):
            print("")
            print(f"Has ganado! efectivamente la palabra era {random_Word}")
            break
        elif (trys == 0):
            print("")
            print(f"Has perdido! la palabra era {random_Word}")
            break

        print("estado actual: " + showed_Word)
        print("")

        letter = input("Adivina una letra: ")
        if (len(letter) != 1):
            while (len(letter) != 1):
                print("Debes ingresar una letra!")
                letter = input("Adivina una letra: ")

        if (letter in guessed_Letters):
            while (letter in guessed_Letters):
                print("Esta letra ya la adivinaste!")
                letter = input("Adivina una letra: ")

        if (letter in random_Word):
            print(f"Adivinaste! {letter} está en la palabra")
            guessed_Letters.append(letter)
        else:
            print(f"Incorrecto! {letter} no está en la palabra... Pierdes una vida")
            trys -= 1
            print(f"Te quedan {trys} vidas")

    repeat = ""
    repeat_Game(repeat)




"""Programa principal"""    

import random

word_List = ["enzo", "rudolfo", "max", "gualter", "nachoman"]

play_Ahorcado()