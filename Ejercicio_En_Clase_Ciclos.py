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