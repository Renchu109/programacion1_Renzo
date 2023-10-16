import math

#Funcion ejercicio 1 & 3

def dni_Validation(number_dni):
    if ((len(number_dni) == 7) or (len(number_dni) == 8)):
        return True
    else:
        return False

#Funcion ejercicio 2

def long_String(a, b):

    for i in range(b):
        if (i == b-1):
            last_Word_Long = len(a[i])

    return last_Word_Long

#Funcion ejercicio 3

def find_Lastname(a):
    for i in range(len(a)):
        if (i == (len(a) - 1)):
            b = len(a[i])

    return b

#Funcion ejercicio 4

def multiplo(a,b):
    if ((a % b) == 0):
        c = True
    else:
        c = False

    return c

#Funcion ejercicio 5

def media_Temp(a,b):
    return (a+b) /2

#Funcion ejercicio 6

def spaced_String(text):
    text.split()

    for i in range(len(text)):
        text[i].split()
        print(text[i], end=" ")

#Ejercicio 7

def the_Max(cad):
    return max(cad)

def the_Min(cad2):
    return min(cad2)

#Ejercicio 8

def calculate_Area(a):
    return math.pi*a*a

def calculate_Per(b):
    return math.pi*b*2

#Ejercicio 9

def login(user, pas, count):
    if ((user == "usuario1") and (pas == "asdasd")):
        log = True
        return True
    else:
        count += 1
        return count
    
#Ejercicio 10

def supermarket(prices, perc):
    desc = {}
    final_Price = {}
    for i in range(len(prices)):
        desc[i+1] =  (perc[i+1] * prices[i+1]) / 100
        final_Price[i+1] = prices[i+1] - desc[i+1]

    return final_Price

#Ejercicio 11

def funcion1(lista):
    lista_Mod = " / ".join(lista)
    return lista_Mod

def funcion2(funcion):
    list = ["enzo", "udolfo", "max", "nachoman", "gualter"]
    print("Primera lista sin modificar: ", list)
    return funcion(list)

#Ejercicio 12

def modify_Phrase(phrase):
    list = phrase.split()
    dic = {}

    for i in range(len(list)):
        dic[i] = {list[i]:len(list[i])}
    return dic

#Ejercicio 13

def calculate_Vector(x,y,z):
    result = math.pow((math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2)), 0.5)
    return (result)

#Ejercicio 14

def cousin(number):
    counter = 0
    for i in range(number):
        if (number % (i+1) == 0):
            counter += 1
        
    if (counter > 2):
        primo = False
    else:
        primo = True

    return primo

#Ejercicio 15

def factorizador(number):
    fac = 1
    while (number > 0):
        fac *= number
        number -= 1
    return fac

#Ejercicio 16, 17

def busdig(dig_,number_):#La cantidad de veces q sale el digito",dig," busting(int,int)
    con=0              
    for i in str(number_):
        if (i==str(dig_)):
            con+=1
    return con

def prime(number_):# ver si es primo o no (number=int)
    if((number_%2)!=0 and (number_%3)!=0 and (number_%5)!=0 or number_==2 or number_==3):
        return True
    else:
        return False

#Ejercicio 17

def ultimapa(fraction):
        fraction=fraction.split()
        amout=(len(fraction))-1
        return len(fraction[amout])
    
def primadd(number): # suma digitos de un numero number= (int)
    number_=number
    aux=0
    sum=0
    while(number_>0):
        aux=int(number_%10)
        sum+=aux
        number_/=10
        
    return sum

def factorial(number_): #saca el factorial de un numero ingresado (number_=int)
    if (number_==1):
        return 1
    elif(number_==2):
        return 2   
    else:
        return (number_*factorial(number_-1))
    
def suma(a,b):
    return (a+b)