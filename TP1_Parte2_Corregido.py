"""Trabajo Práctico 1: parte 2"""

"""Renzo Di Laudo, comisión B"""


"""Ejercicio 1"""


print("Calcular el perímetro y área de un rectángulo dada su base y su altura")
base = float(input("Ingresar base: "))
altura = float(input("Ingresar altura: "))
    
area = base * altura
perimetro = base * 2 + altura * 2
print("El área del rectángulo es: ",area)
print("El perímetro del rectángulo es: ",perimetro)


"""Ejercicio 2"""


cateto1 = float(input("Ingresa cateto 1: "))
cateto2 = float(input("Ingresa cateto 2: "))
print("cateto 1 es: "+str(cateto1))
print("cateto 2 es: "+str(cateto2))
hipo = (cateto1**2 + cateto2**2)**1/2
print("La hipotenusa es: ",hipo)


"""Ejercicio 3"""


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")


"""Ejercicio 4"""


farenheit = int(input("Ingrese temperatura (farenheit): "))
celcius = (farenheit - 32) * 5/9
print("En celcius: ",celcius, "°")


"""Ejercicio 5"""


"""5a"""

cancion = input("¿Cuál es su canción favorita? ")

"""5b"""

precio = int(input("Precio: "))
total = precio + (precio * 0.1)
print("Precio final: ",total)


"""5c"""

edad = int(input("Edad: "))
print("Tu edad es",edad)

"""5d"""

edad = int(input("Edad: "))
print("Veamos si tu edad es 18... ", edad == 18)


"""Ejercicio 6"""


num1 = int(input("Ingrese un primer número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))

media = (num1 + num2 + num3) / 3

print("La media de ",num1, ",",num2, " y ",num3, " es: ",media )


"""Ejercicio 7"""


min = int(input("Ingrese minutos: "))
hours = int(min / 60)
min2 = min % 60
print(f"{hours}:{min2}")


    """Ejercicio 8"""


sueldo = int(input("Ingrese su sueldo: "))
ventas = 3
comision = sueldo * .1

total = sueldo + (ventas * comision)

print("Su sueldo final es de: $",total)


"""Ejercicio 9"""


precio = float(input("Ingrese el precio del producto: "))
descuento = precio * .15
precio = precio - descuento

print("El total a abonar por su producto es de: $",precio)


"""Ejercicio 10"""


parcial_1 = int(input("Ingrese su primera nota: "))
parcial_2 = int(input("Ingrese su segunda nota: "))
parcial_3 = int(input("Ingrese su tercera nota: "))

examen_final = int(input("Ingrese su nota del examen final: "))

trabajo_final = int(input("Ingrese su nota del trabajo final: "))

promedio_parciales = (parcial_1 + parcial_2 + parcial_3) / 3

calificacion_final = (promedio_parciales * .55) + (examen_final * .30) + (trabajo_final * .15)

print("Su calificacion final es: ",calificacion_final)


"""Ejercicio 11"""


num1 = int(input("Ingrese un primer numero: "))
num2 = int(input("Ingrese un segundo numero: "))

distancia = abs(num1 - num2)

print(f"La distancia entre {num1} y {num2} es {distancia}")


"""Ejercicio 12"""


num = int(input("Ingrese un número: "))

raiz_cuad = num**(1/2)

raiz_cub = num**(1/3)

print(f"La raiz cuadrada de {num} es {raiz_cuad} y su raiz cúbica es {raiz_cub}")


"""Ejercicio 13"""


num = int(input("Introduzca un número de dos cifras: "))

primero = int(num / 10)
segundo = num % 10

print(f"{num} invertido es: ",str(segundo) + str(primero))


"""Ejercicio 14"""


a = int(input("Número A: "))
b = int(input("Número B: "))

c = a
a = b
b = c

print(f"Número A:{a} Número B:{b}")


"""Ejercicio 15"""


hours = int(input("Hora: "))
min = int(input("Minutos: "))
sec = int(input("Segundos: "))
print(f"Hora de salida {hours}:{min}:{sec}")

t = int(input("Tiempo de viaje (segundos): "))

hours2 = int(t / 3600)
min2 = int((t % 3600) / 60)
sec2 = int(t % 60)

total_hours = hours + hours2
total_min = min + min2
total_sec = sec + sec2

if (total_sec >= 60):
    total_sec = total_sec - 60
    total_min = total_min + 1  
    if (total_min >= 60):
        total_min = total_min - 60
        total_hours = total_hours + 1
        if (total_hours >= 24):
            total_hours = total_hours - 24

print(f"Hora de llegada: {total_hours}:{total_min}:{total_sec}")


"""Ejercicio 16"""


nombre = str(input("Ingrese su nombre: "))
primer_ape = str(input("Ingrese su primer apellido: "))
segundo_ape = str(input("Ingrese su segundo apellido: "))

iniciales = print(f"Iniciales: {nombre[0]}.{primer_ape[0]}.{segundo_ape[0]}.")


"""Ejercicio 17"""


usuario = str(input("Usuario, ingrese su nombre: "))

print("Ahora estás en la matrix,",usuario)


"""Ejercicio 18"""


cuenta = float(input("Ingrese el monto de la cuenta: $"))
servicio = cuenta * .062
propina = cuenta * 0.1

total = cuenta + servicio + propina

print(f"El total a abonar es de: ${total}")


"""Ejercicio 19"""


dia_nac = int(input("Ingrese su día de naciomiento: "))
mes_nac = int(input("Ingrese su mes de naciomiento: "))
anio_nac = int(input("Ingrese su año de naciomiento: "))

print(f"{dia_nac}/{mes_nac}/{anio_nac}")


"""Ejercicio 20"""


fecha = input("Ingrese su fecha de nacimiento (DDMMAAAA): ")
print(fecha[0:2],"/",fecha[2:4],"/",fecha[4:8])


"""Ejercicio 21"""


kilometros_litro = float(input("Ingrese los kilómetros que recorre la moto por litro de gasolina: "))
cap_tanque = int(input("Ingrese la capacidad del tanque (litros): "))
kilometros_viaje = float(input("Ingrese los kilómetros a recorrer: "))

cant_tanques = kilometros_viaje / (kilometros_litro * cap_tanque)

if cant_tanques % 1 != 0:
    print(f"Necesitarán {(cant_tanques - cant_tanques % 1) + 1} tanques")
else:
    print(f"Necesitarán {cant_tanques} tanques")   
