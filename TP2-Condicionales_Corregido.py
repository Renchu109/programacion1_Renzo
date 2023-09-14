#Trabajo Práctico 2 - Condicionales



#Ejercicio 1 & 2

edad = int(input("Ingrese la edad de la computadora: "))

if (edad <= 2 and edad >= 0):
    print("La computadora es nueva")
elif (edad > 2):
    print("La computadora es vieja")
else:
    print("La edad ingresada no es válida")

#Ejercicio 3

nombre_1 = str(input("Ingrese el nombre de una persona: "))
nombre_2 = str(input("Ingrese el nombre de otra persona: "))

if (nombre_1[0:1] == nombre_2[0:1]):
    print("Coincidencia")
else:
    print("No hay coincidencia")

#Ejercicio 4

voto = str(input("elija a un candidato (A,B o C): "))
voto = voto.upper()

if (voto == "A"):
    print("Usted votó por el partido rojo")
elif(voto == "B"):
    print("Usted votó por el partido verde")
elif(voto == "C"):
    print("Usted votó por el partido azul")
else:
    print("Opción errónea")

#Ejercicio 5

letra = str(input("Ingrese una letra: "))
letra = letra.lower()

if (len(letra) != 1):
    print("No se puede procesar el dato")
elif (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
    print("Es una vocal")
elif (letra != "a" or letra != "e" or letra != "i" or letra != "o" or letra != "u"):
    print("No es vocal")

#Ejercicio 6

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0 and anio % 400 != 0):
    print("Es año bisiesto")
elif (anio % 100 == 0 and anio % 400 == 0):
    print("Es año bisiesto")
else:
    print("El año ingresado no es bisiesto")

#Ejercicio 7

num_1 = int(input("Ingrese un primer número: "))
num_2 = int(input("Ingrese un segundo número: "))
num_3 = int(input("Ingrese un tercer número: "))

menor = num_1

if (num_2 < menor and num_2 < num_3):
    menor = num_2
elif (num_3 < menor and num_3 < num_2):
    menor = num_3

print("El menor es:",menor)

#Ejercicio 8

nombre_usuario = str(input("Ingrese un nombre de usuario: "))
contrasenia = str(input("Ingrese la contraseña: "))

if (nombre_usuario == "Gwenevere" and contrasenia == "excalibur"):
    print("Usuario y contraseña correctos, puede ingresar a Camelot")
elif (nombre_usuario == "Gwenevere" and contrasenia != "excalibur"):
    print("Usuario correcto, contraseña incorrecta")
elif (nombre_usuario != "Gwenevere" and contrasenia == "excalibur"):
    print("Usuario incorrecto, contraseña correcta")
else:
    print("Acceso denegado")

#Ejercicio 9

nombre = str(input("Ingrese el nombre del alumno: "))
sexo = str(input("Ingrese el sexo del alumno hombre/mujer: "))

inicial = nombre[0]

nombre = nombre.lower()
sexo = sexo.lower() 
inicial = inicial.lower()

if (inicial < "m" and sexo == "mujer"):
    print("Grupo A")
elif (inicial > "n" and sexo == "hombre"):
    print("Grupo A")
else:
    print("Grupo B")

#Ejercicio 10 

edad=int(input("ingresar edad: "))
if(edad<4):
    print("Puede entrar gratis")
elif(edad>=4 or edad<=18):
    print("Tiene que pagar $500")
elif(edad>18):
    print("Tiene que pagar $1000")



#Ejercicio 11 

print("Bienvenido a la pizzeria Bella Napoli")
orden=input("¿Quiere el menu vegetariano? si/no ")
orden=orden.lower()
if(orden=="si" or orden =="s"):
     print("Ingredientes vegetarianos:")
     print(".Pasto")
     print(".Pimiento")
     print(".Tofu")
elif(orden=="no" or orden =="n"):
    print("Ingredientes no vegetarianos:")
    print(".Peperoni")
    print(".Jamón")
    print(".Salmón")

ingre=input("Que ingrediente quiere? ")
if(orden=="si" or orden =="s"):
     print("Su pizza vegetariana tiene: mozzarella, tomate y",ingre)
elif(orden=="no" or orden =="n"):
     print("Su pizza tiene: mozzarella, tomate y",ingre)

# Ejercicio 12 

anio_actual = int(input("Ingrese el año actual: "))
anio = int(input("Ingrese otro año: "))
pasaron = anio_actual - anio
falta = anio - anio_actual
if (anio_actual > anio):
    print(f"Pasaron {pasaron} años.")
elif (anio_actual < anio):
    print(f"Faltan {falta} años.")
else:
    print("Es el mismo año.")

# Ejercicio 13 

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
mayor = 0
menor = 0

if (num1 < 0 or num2 < 0):
    print("Ingresó un número negativo.")

if (num1 > num2):
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

if (mayor == 0 or menor == 0):
    print("0 sólo es múltiplo de 0")
else:
    if (mayor % menor == 0):
        print("Son múltiplos.")
    elif (mayor % menor != 0):
        print("No son múltiplos.")


#Ejercicio 14 

print("Ingrese los coeficientes de una ecuación de primer grado (a x + b = 0)")

coe_a=int(input("Ingrese ¨a¨ (a debe ser distinto de 0)"))

if (coe_a != 0):
    coe_b=int(input("Ingrese ¨b¨ "))

    respues_=-coe_b/coe_a
    coe_a=str(coe_a)
    coe_b=str(coe_b)
    respues_=str(respues_)
    
    print("El valor de x es: "+respues_)
    print("La formula quedaria: "+coe_a
        +"*"+respues_+"+"+coe_b+"="+"0")
else:
    print("a debe ser distinto de 0")

#Ejercicio 15: 

import math

print("c: area de un circulo / t: area de un triangulo")

operacion = input("¿Que operaciòn desea realizar?: ")
operacion = operacion.lower()

if operacion == "t":
  base = int(input("Ingrese base: "))
  altura = int(input("Ingrese altura: "))
  print(f"Resultado: {(base*altura)/2}")
elif operacion == "c":
  radio = int(input("Ingrese radio: "))
  print(f"Resultado: {round(math.pi * radio**2, 2)}")
else:
    print("Operacion invalida")

#Ejercicio 16:  

valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))

print("1. Suma, 2. Multiplicaciòn, 3. Resta, 4. Division")

operacion = int(input("Operacion que desea realizar: "))

if operacion == 1:
  print(f"Resultado: {valor1 + valor2}")
elif operacion == 2:
  print(f"Resultado: {valor1 * valor2}")
elif operacion == 3:
  print(f"Resultado: {valor1 - valor2}")
elif operacion == 4:
  if (valor2 == 0):
    print("No se puede dividir por 0")
  else:
    print(f"Resultado: {valor1 / valor2}")
else:
  print("Operacion invalida")


#Ejercicio 17: 

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
mensaje_dia = ["Feliz Lunes", "Buen Martes", "Que lindo Miercoles", "Dia Jueves", "Hoy es Viernes", "Sabado, hoy se sale", "Domingo, hoy se duerme"]

dia_semana = input("Ingrese dia de la semana: ")
dia_semana = dia_semana.lower()

if dia_semana not in dias_semana:
  print("El dia ingresado no es un dia valido")
else:
  if dia_semana == dias_semana[0]:
    print(mensaje_dia[0])
  elif dia_semana == dias_semana[1]:
    print(mensaje_dia[1])
  elif dia_semana == dias_semana[2]:
    print(mensaje_dia[2])
  elif dia_semana == dias_semana[3]:
    print(mensaje_dia[3])
  elif dia_semana == dias_semana[4]:
    print(mensaje_dia[4])
  elif dia_semana == dias_semana[5]:
    print(mensaje_dia[5])
  else:
    print(mensaje_dia[6])

# Ejercicio 18:

horas_trabajo = int(input("Ingrese cantidad de horas trabajadas en el mes: "))
salario_hora = int(input("Ingrese salario por hora: "))

if horas_trabajo > 48:
  hora_extra = horas_trabajo - 48
  trabajo_minimo = salario_hora * 48
  pago_extra = hora_extra * salario_hora
  ingreso_total = trabajo_minimo + pago_extra + (pago_extra * .10)
  print(f"Salario total: ${round(ingreso_total)}")
else:
  ingreso_total = salario_hora * horas_trabajo
  print(f"Salario total: ${round(ingreso_total)}")

#Ejercicio 19:

precio_lapiz = 60
descuento = .7

cantidad_lapices = int(input("Ingrese cantidad de lapices: "))

if (cantidad_lapices >= 1000):
    total = precio_lapiz * cantidad_lapices
    precio_final = total - (total * descuento)
    print(f"Precio final: ${round(precio_final)}")
elif (cantidad_lapices < 1000):
    precio_final = precio_lapiz * cantidad_lapices
    print(f"Precio final: ${precio_final}")


#Ejercicio 20

pre_notas = input("Ingrese nota 1: ") + "," + input("Ingrese nota 2: ") + "," + input("Ingrese nota 3: ") + "," + input("Ingrese nota 4: ")

nota1, nota2, nota3, nota4 = pre_notas.split(",")

promedio = (int(nota1) + int(nota2) + int(nota3) + int(nota4)) / 4

if promedio >= 6:
  print(f"Nota: {round(promedio, 2)}, Aprobado")
else:
  print(f"Nota: {round(promedio, 2)}, Desaprobado")
