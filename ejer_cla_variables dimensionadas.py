#Ejercicio 1
"""
def addpassenger():
    name=input("Ingresar nombre del pasajero: ")
    dni=input("Ingresar DNI: ")
    destination_=input("Destino: ")
    
    aux=(name, dni, destination_)
    return aux


def addcity(city_, local_):
    aux_=(city_,local_)
    return aux_

def travel(dni__,passengers_):
    for i in passengers_:
       if(i[1]==dni__):
           travel_=i[2]
           
    return travel_

def getpassenger(city_,passengers_):
    cont=0
    for i in passengers_:
        if(i[2]==city_):
            cont+=1
    return cont

def getpassenger2(pais,passengers_,destination_):
    cont=0
    for i in destination_:
        if(i[1]==pais):
            city_=i[0]
    
    for i in passengers_:
        if(i[2]==city_):
            cont+=1
    return cont

def travel2(dni__,passengers_,destination_):
    for i in passengers_:
        if(i[1]==dni__):
           travel_=i[2]
    for j in destination_:
        if(j[0]==travel_):
            return j[1]       
    

destination=[]
passengers=[]

while(True):
    print("-----------------------------------------------------------------------------")
    print("A) Agregar pasajero")
    print("B) Agrega ciudades a la lista de ciudades")
    print("C) Dado DNI de un pasajero, ver a que ciudad viaja")
    print("D) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("E) Dado el DNI de un pasajero ,ver a que pais viaja")
    print("F) Dado un pais, mostrar cuantos pasajeros viajan a ese pais")
    print("exit) para salir.") 
    option=(input("ingresar opcion: ")).lower()
    if(option=="exit"):
        print("Saliendo del programa")
        break
    elif(option=="a"):#se quiere agregar un pasajero
        print("------------------------------------------------------")
        passengers.append(addpassenger())
        aux=False  

        city=passengers[len(passengers)-1]#busca el pasajero q se agrego 
        city=city[2]#saca la ubicacion del pasajero 
        
        for i in destination:#recorro la ubicaciones guardadas, para ver si coincide con la ubicacion del ultimo pasajero agregado
            if(i[0]==city):
                aux=True
        
        if(aux==False):#si no esta creada en la ubicaciones guardadas, la agrego
            local=input("A que ciudad pertenece "+city+"? ")
            destination.append(addcity(city, local))
                        
    elif(option=="b"):#se quiere agregar una ciudad
        print("------------------------------------------------------")
        city=input("Agregar ciudad: ")
        local=input("Agregar pais: ")
        destination.append(addcity(city, local))
    elif(option=="c"):
        print("------------------------------------------------------")
        dni_=input("ingresar DNI para buscar destino ")
        desti=travel(dni_,passengers)
        print("El usuario con el DNI "+dni_+" tiene como destino "+desti)     

    elif(option=="d"):
        print("------------------------------------------------------")
        city=input("Ingresar una ciudad para ver la cantidad de personas que viajan a ella: ")
        print("La cantidad de personas que viajan a la ciudad "+city+" es de:",getpassenger(city,passengers))

    elif(option=="e"):
        print("------------------------------------------------------")
        dni_=input("ingresar DNI para buscar destino ")
        desti=travel2(dni_,passengers,destination)
        print("El usuario con el DNI "+dni_+" tiene como destino el pais "+desti)
    
    elif(option=="f"):
        print("------------------------------------------------------")
        pais=input("Ingresar un pais para ver la cantidad de personas que viajan a el: ")
        print("La cantidad de personas que viajan al pais "+pais+" es de:",getpassenger2(pais,passengers,destination))
"""

#Ejercicio 2
"""
def sendinvoice(shopping_):
    home=[]
    home_=[]
    for i in shopping_:
        home.append(i[3])
                    
    for i in home:
        if i not in home_:
            home_.append(i)
    return home_                              
#[(cliente, dia del mes, monto, domiciolio del cliente)]
shopping=[("Nuria Costa", 5, 1234.5,"Calle 1 – 456"), ("Jorge Russo", 7, 3999, "Calle 2 – 741"),("Nuria Costa", 5, 2000,"Calle 1 – 456")]

home=sendinvoice(shopping)

for i in home:
    print("mandar factura a:",i)
"""    


#Ejercicio 3
#Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día
#Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día


def show(partners_):
    for i, value in partners_.items():
        print("-----------------------------")
        print("socio",i)
        for key_, val in value.items():
            print(key_+": "+val) 

def amount(partners_):
    con=0          
    for i in partners:
        con+=1
    return con     

def notify_payment(numberso_,partners_):
    print(partners[numberso_]["cuota al dia"])
    partners_[numberso_]["cuota al dia"]="si"
    print("se actualizo el pago de socio "+partners_[numberso_]["nombre"])
    return partners_

def Changedate(partners_):
    for key, value in partners_.items():
        if(value["ingreso"]=="17/03/2009"):
            partners_[key]["ingreso"]="14/03/2018"
            print("Se cambio la feca de ingres de "+value["nombre"]+" de 17/03/2009 al 14/03/2018")

def deletpartner(partners_,name_):
    for key, value in partners_.items():
        if((value["nombre"]).lower()==name_):
            del partners_[key]
            return partners_
    print("No se encontro el nombre")
    return partners_        

def addpartners(partners_):
    aux=len(partners_)+1
    name=input("ingresar nombre: ").title()
    date=input("ingresar fecha formato(dd/mm/aaaa): ")
    
    partners_[aux]={"nombre":name, "ingreso":date,"cuota al dia":"si"}
    return partners_


partners={"1":{"nombre":"Amanda Núñez","ingreso":"17/03/2009","cuota al dia":"si"},
          "2":{"nombre":"Bárbara Molina", "ingreso":"17/03/2009","cuota al dia":"si"},
          "3":{"nombre":"Lautaro Campos", "ingreso":"17/03/2009","cuota al dia":"si"},
          }  


while True:
    print("A) Mostrar ")
    print("B) Ver cantidad de socios")
    print("C) Notificar pago")
    print("D) Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018")
    print("E) Eliminar un socio")
    print("EXIT) salir del menu")
    option=(input()).lower()
    if(option=="a"):
        show(partners)
        print("-----------------------------")
    
    elif(option=="b"):
        print("Cantidad de socios:",amount(partners))
        print("-----------------------------")
    
    elif(option=="c"):
        numberso=input("Ingresar numero de socio para notificar el pago: ")
        partners=notify_payment(numberso,partners)
        print("-----------------------------")
    elif(option=="d"):
        Changedate(partners)
        print("-----------------------------")
    elif(option=="e"):
        name=(input("Ingresar nombre y apellido del socio a eliminar ")).lower()    
        partners=deletpartner(partners, name)
        print("-----------------------------")
    elif(option=="f"):
        partners=addpartners(partners)
        print("-----------------------------")
    elif(option=="exit"):
        print("chau, saliendo del progama... ")
        break    