
#Ejercicios en clase - Condicionales


#Solicito ingreso de fecha formato "día, DD/MM" , permitiendo uso de mayúsculas
fecha = input("Ingrese la fecha (formato día, DD/MM): ")
print(fecha.lower())

#Asigno a variables (str e int) a los datos ingresados por el usuario en el bloque de códigos anterior
dia_sem = fecha [0:fecha.find(",")]
dia = int(fecha[fecha.find(" ") + 1:
            fecha.find("/")])
mes = int(fecha[fecha.find("/") + 1:])
dia_sem = dia_sem.lower()

#corroboro que la fecha ingresada sea válida 
if (dia_sem != "lunes" and dia_sem != "martes" and dia_sem != "miercoles" and dia_sem != "jueves" and dia_sem != "viernes" ):
    print("Dia incorrecto")
elif (dia < 1 or dia > 31):
    print("Fecha (dia) incorrecta")
elif (mes < 1 or mes > 12):
    print("Fecha (mes) incorrecta")
else:
    print("Fecha ingresada válida") 


#Secuencia de acciones a seguir según el día ingresado
if (dia_sem == "lunes"):
    print("Nivel inicial")
    #Corroborar si se tomaron exámenes
    dec = str(input("¿Se tomaron exámenes? "))
    #Acciones si se tomaron exámenes
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    #Acciones si no se tomaron exámenes
    else:
        print("No se tomaron exámenes")
elif (dia_sem == "martes"):
    print("Nivel intermedio")
    #Corroborar si se tomaron exámenes
    dec = str(input("¿Se tomaron exámenes? "))
    #Acciones si se tomaron exámenes
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    #Acciones si no se tomaron exámenes
    else:
        print("No se tomaron exámenes")
elif (dia_sem == "miercoles"):
    print("Nivel avanzado")
    #Corroborar si se tomaron exámenes
    dec = str(input("¿Se tomaron exámenes? "))
    #Acciones si se tomaron exámenes
    if (dec == "si"):
        alu_aprob = int(input("Ingrese el número de alumnos aprobados: "))
        alu_desaprob = int(input("Ingrese el número de alumnos desaprobados: "))
        total = alu_aprob + alu_desaprob
        print(f"El porcentaje de aprobados es {(alu_aprob / total) * 100} %")
    #Acciones si no se tomaron exámenes
    else:
        print("No se tomaron exámenes")
elif (dia_sem == "jueves"):
    print("Práctica hablada")
    #Acciones para el día jueves (asistencia)
    asistencia = int(input("Ingrese el porcentaje de alumnos que asistieron a clase: %"))
    if (asistencia > 50):
        print("Asistió la mayoría")
    elif (asistencia < 50):
        print("No asistió la mayoría")
    else:
        print("Asistió la mitad del curso")    
else:
    print("Inglés para viajeros")
    #Acciones para el día viernes (comienzo de ciclo, arancel x alumno, arancel total)
    if (dia == 1 and (mes == 1 or mes == 7)):
        print("Comienzo de nuevo ciclo")
        alu_nuev = int(input("Ingrese cantidad de alumnos del nuevo ciclo: "))
        alu_arancel = int(input("Ingrese el arancel por cada alumno: $"))
        tot_arancel = print(f"El ingreso total es de ${alu_arancel * alu_nuev}")
    else:
        print("Ciclo comenzado")
