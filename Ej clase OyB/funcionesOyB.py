#Funciones ejercicio en clase O y B

#Método burbuja
def ordenamiento_burbuja(arr):
    n = len(arr)
    
    # Itera a través de todos los elementos de la lista
    for i in range(n):
        # Bandera para optimizar; si no se realiza ningún intercambio en un pase, la lista está ordenada
        intercambio_realizado = False
        
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente elemento, haga el intercambio
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio_realizado = True
        
        # Si no se realizó ningún intercambio en este pase, la lista está ordenada y podemos salir
        if not intercambio_realizado:
            break

#Método por selección
def ordenamiento_seleccion(arr):
    n = len(arr)
    
    # Itera a través de todos los elementos de la lista
    for i in range(n):
        # Encuentra el índice del elemento mínimo restante en la lista no ordenada
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        
        # Intercambia el elemento actual con el elemento mínimo encontrado
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

#Metodo por inserión
def ordenamiento_insercion(arr):
    n = len(arr)

    # Recorremos la lista desde el segundo elemento hasta el último
    for i in range(1, n):
        elemento_actual = arr[i]

        # Mueve elementos de arr[0..i-1], que son mayores que elemento_actual, a una posición adelante de su posición actual
        j = i - 1
        while j >= 0 and elemento_actual < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elemento_actual

#Método Merge sort
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        medio = len(arr) // 2
        mitad_izquierda = arr[:medio]
        mitad_derecha = arr[medio:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        # Copiar datos a listas temporales mitad_izquierda y mitad_derecha
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1

        # Comprobar si quedan elementos por copiar en ambas mitades
        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1