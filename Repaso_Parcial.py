exit=False
customer=int(input("¿cuantas personas son?: "))
for i in range(customer):
    #comida
    menuquote=""
    #precio total comida
    food_price=0
    #bebidas
    drinks_menu=""
    #precio total bebidas
    drinks_price=0
    #postres total
    dessert_menu=""
    #precio total postres
    dessert_price=0
    while(exit==False):
        print("Menu")
        print("Bienvenido al restaurante 5 estrellas: La Maxiggiana")
   
        print("Ingrese una opción para continuar.")
        print("1). Ver plato principal.")
        print("2) Ver bebidas.")
        print("3) Ver postres.")
        print("0) para terminar con el pedido")
        option=(int(input()))
        if(option==0):
            break
        #opcion de plato principal
        if(option==1):
            #var para guardar pedido
           
            #var para guardar total de precio
           
            while (1>0):
               #menu de lo que puede pedir de plato principal y sus variantes
                print("Menu de comidas")
                print("1) Milanesa ")
                print("2) Pollo $1800")
                print("3) Asado $3600")
                print("4) spaghetti  $2500")
                print("5) Ravioles $2700")
                print("6) Pastel de papa $3000 ")
                print("0) Para salir")
                option_=int(input())
                if(option_==0):
                    break
                #entra a la opcion de milanesas
                if(option_==1):
                    #variante de milanesas
                    print("1)Milanesa de pollo $1500")
                    print("2)Milanesa de carne $2000")
                    aux=int(input())
                    #se agrega al pedido y se suma el precio
                    if(aux==1 and menuquote!=""):
                        menuquote=menuquote+", Milanesa de pollo"
                        food_price+=1500
                    elif(aux==1 and menuquote==""):    
                        menuquote=menuquote+"Milanesa de pollo"
                        food_price+=1500
                    elif(aux==2 and menuquote==""):
                        menuquote=menuquote+"Milanesa de carne"
                        food_price+=2000    
                    elif(aux==2 and menuquote!=""):
                        menuquote=menuquote+", Milanesa de carne"
                        food_price+=2000
                # entra a la opcion de pollo
                elif(option_==2):
                    if(menuquote==""):
                        menuquote=menuquote+"Pollo"
                        food_price+=1800
                    else:
                        menuquote=menuquote+", Pollo"
                        food_price+=1800
                # entra a la opcion de asado
                elif(option_==3):
                    if(menuquote==""):
                        menuquote=menuquote+"Asado"
                        food_price+=3600
                    else:
                        menuquote=menuquote+", Asado"
                        food_price+=3600    
                # Entra en sphagetti
                elif(option_==4):
                    #variante de sphagetti
                    print("1)Sin salsa")
                    print("2)Con salsa ")
                    print("3)con salsa blanca")  
                    print("4)Con salsa bolognesa (costo extra de $300)")
               
                    option_=int(input())
                    #option solo
                    if(option_==1 and menuquote=="" ):
                        menuquote=menuquote+"spaghetti "
                        food_price+=2500
                    elif(option_==1 and menuquote!=""):
                        menuquote=menuquote+", spaghetti"
                        food_price+=2500
                    #option con salsa
                    elif(option_==2 and menuquote=="" ):
                        menuquote=menuquote+"Spaghetti con salsa"
                        food_price+=2500
                    elif(option_==2 and menuquote!=""):
                        menuquote=menuquote+", soaghetti con salsa"
                        food_price+=2500  
                    #con salsa blanca
                    elif(option_==3 and menuquote=="" ):
                        menuquote=menuquote+"Spaghetti con salsa"
                        food_price+=2500
                    elif(option_==3 and menuquote!=""):
                        menuquote=menuquote+", soaghetti con salsa"
                        food_price+=2500  
                    #con salsa bolognesa
                    elif(option_==2 and menuquote=="" ):
                        menuquote=menuquote+"Spaghetti con salsa bolognesa"
                        food_price+=2800
                    elif(option_==2 and menuquote!=""):
                        menuquote=menuquote+", soaghetti con salsa bolognesa"
                        food_price+=2800            
                #entra en ravioles
                elif(option_==5):
                    if(menuquote==""):
                        menuquote=menuquote+"Ravioles"
                        food_price+=2700
                    else:
                        menuquote=menuquote+", Ravioles"
                        food_price+=2700
                #entra en Pastel de papa $3000
                elif(option_==6):
                    if(menuquote==""):
                        menuquote=menuquote+"Pastel de papa"
                        food_price+=3000
                    else:
                        menuquote=menuquote+", Pastel de papa"
                        food_price+=3000  
        ##entra en bebidas
        elif(option==2):
            while(1>0):
                print(" Menu Bebidas")
                print("1) Cocacola 500ml $500")
                print("2) Cocacola 1l $700")
                print("3) Sprite 500ml $500")
                print("4) Sprite 1l $700")
                print("0) para salir del menu bebidas")
                aux=int(input())
                #opciom 1
                if(aux==0):
                    break
                elif(aux==1 and drinks_menu==""):
                    drinks_menu=drinks_menu+"Cocacola 500ml"
                    drinks_price+=500
                elif(aux==1 and drinks_menu!=""):
                    drinks_menu=drinks_menu+", Cocacola 500ml"
                    drinks_price+=500
                #opcion 2
                elif(aux==2 and drinks_menu!=""):
                    drinks_menu=drinks_menu+", Cocacola 1l"
                    drinks_price+=700
                elif(aux==1 and drinks_menu==""):
                    drinks_menu=drinks_menu+"Cocacola 1l"
                    drinks_price+=700
                #opcion 3
                elif(aux==2 and drinks_menu!=""):
                    drinks_menu=drinks_menu+", Sprite 500ml"
                    drinks_price+=500
                elif(aux==2 and drinks_menu==""):
                    drinks_menu=drinks_menu+"Sprite 500ml"
                    drinks_price+=500
                #opcion 4
                elif(aux==2 and drinks_menu!=""):
                    drinks_menu=drinks_menu+", Sprite 1l"
                    drinks_price+=700
                elif(aux==2 and drinks_menu==""):
                    drinks_menu=drinks_menu+"Sprite 1l"
                    drinks_price+=700                
        ##entra en postres
        elif(option==3):
            while(1>0):
                print(" Menu postres")
                print("1) Flan $500")
                print("2) ChoriFlan $700")
                print("3) Helado $500")
                print("4) Ensalada de frutas $700")
                print("0) para salir")
                aux=int(input())
                #opcion 0 sale del menu
                if(aux==0):
                    break
                #opciom 1
                elif(aux==1 and dessert_menu==""):
                    dessert_menu=dessert_menu+"Flan"
                    dessert_price+=500
                elif(aux==1 and dessert_menu!=""):
                    dessert_menu=dessert_menu+", Flan"
                    dessert_price+=500
                #opcion 2
                elif(aux==2 and dessert_menu!=""):
                    dessert_menu=dessert_menu+", ChoriFlan"
                    dessert_price+=700
                elif(aux==1 and dessert_menu==""):
                    dessert_menu=dessert_menu+"ChoriFlan"
                    dessert_price+=700
                #opcion 3
                elif(aux==2 and dessert_menu!=""):
                    dessert_menu=dessert_menu+", Helado"
                    dessert_price+=500
                elif(aux==2 and dessert_menu==""):
                    dessert_menu=dessert_menu+"Helado"
                    dessert_price+=500
                #opcion 4
                elif(aux==2 and dessert_menu!=""):
                    dessert_menu=dessert_menu+", Ensalada de frutas"
                    dessert_price+=700
                elif(aux==2 and dessert_menu==""):
                    dessert_menu=dessert_menu+"Ensalada de frutas"
                    dessert_price+=700
    #uno los pedidos en uno
    #si menuquote contiene pedido entra
    if(menuquote!=""):
        #si drinks_menu contiene pedido entra
        if(drinks_menu!=""):
            #si dessert_menu contiene pedido entra
            if (dessert_menu!=""):
                menuquote=menuquote+", "+drinks_menu+", "+dessert_menu
            #si dessert_menu no contiene pedido entra
            else:
                menuquote=menuquote+", "+drinks_menu
        #Si drinck_menu no contiene pedido entra
        elif(drinks_menu==""):
            #si dessert_menu contiene pedido entra
            if (dessert_menu!=""):
                menuquote=menuquote+", "+dessert_menu
    #El menuquote no contiene pedido        
    elif(menuquote==""):
        #drink contiene pediodo entra
        if(drinks_menu!=""):
            if (dessert_menu!=""):
                menuquote=drinks_menu+", "+dessert_menu
        #drink no contiene pedido
        elif(drinks_menu==""):
            #desser contiene pedido
            if(dessert_menu!=""):
                menuquote=dessert_menu
            #si ninguna contiene pedido menuquote se queda con valor ""
    #si menuquote contiene pedido lo muestra
    if(menuquote!=""):        
        print("El cliente",(i+1),"pidio "+menuquote+" y costo",food_price )
   
    elif(menuquote==""):
        print("El cliente",(i+1),"no realizo pedido")  