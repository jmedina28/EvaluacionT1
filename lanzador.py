

def iniciador():  
    seleccion = int(input("Introduzca el número de ejercicio que desea ejecutar: "))
    if seleccion == 1:
        from ejer1 import generador1, elemento
        matriz = []
        fila = 0
        dimensiones = int(input("Introduzca el número de filas que desea que tenga su matriz ix4: "))
        generador1(dimensiones)
        elemento(matriz)
        print(matriz)
    elif seleccion == 2:
        from ejer2 import comprobacion
        cadena = input("Introduzca una frase: ")
        lista = list(cadena)
        print(lista)
        print(comprobacion(lista))