


def iniciador():  
    seleccion = int(input("Introduzca el número de ejercicio que desea ejecutar: "))
    if seleccion == 1:
        import ejer1
    elif seleccion == 2:
        from ejer2 import comprobacion
        cadena = input("Introduzca una frase: ")
        lista = list(cadena)
        print(lista)
        print(comprobacion(lista))
    elif seleccion == 3:
        from ejer3 import generador2
        opcion = 1
        for i in range(5):
            print("Opción", opcion, ":", generador2(opcion))
            opcion += 1
    elif seleccion == 4:
        from tabla import generador3
        i = int(input("Introduzca el número de filas que desea que tenga su tabla: "))
        j = int(input("Introduzca el número de columnas que desea que tenga su tabla: "))
        print(generador3(i,j))
        