#Ejercicios en clase ciclos

#Ejercicio 1

abcdario = "abcdefghijklmnñopqrstuvwxyz"

mensaje_encrip = ""
corrimiento = int(input("Ingrese el corrimiento: "))

for i in range(5):
  mensaje = input(f"Ingrese su mensaje del dia {i + 1}: ")
  mensaje_lower = mensaje.lower()

  for j in mensaje_lower:
    letra = abcdario.find(j)
    search = letra + corrimiento

    if search > 26:
      resto = search % 26
      mensaje_encrip += abcdario[resto]
    else:
      mensaje_encrip += abcdario[letra + corrimiento]
  print(f"Tu mensaje es: {mensaje_encrip.upper()}")
  mensaje_encrip = ""

#Ejercicio 2

bool = "true"

pair_Digits = 0
odd_Digits = 0

total_Pair_Digits = 0
total_Odd_Digits = 0

while (bool == "true"):
    number = int(input("Ingrese un número entero cualquiera o ingrese 0 para terminar el ciclo: "))
    if (number != 0):
        if (number < 0):
            number *= -1
        number = str(number)
        long_number = len(number)
        number = int(number)
        for i in range(long_number):
            digit = int((number / 10**(long_number - 1)) % 10)
            if (digit % 2 != 0):
                odd_Digits += 1
                total_Odd_Digits += 1
            else:
                pair_Digits += 1
                total_Pair_Digits += 1
            long_number -= 1
        print(f"El número {number} tiene {pair_Digits} dígitos pares y {odd_Digits} dígitos impares")
        pair_Digits = 0
        odd_Digits = 0
    else:
        print("Ciclo terminado")
        print(f"Total de dígitos pares: {total_Pair_Digits}")
        print(f"Total de dígitos impares: {total_Odd_Digits}")
        bool = "false"
