

def iniciador():  
    seleccion = int(input("Introduzca el número de ejercicio que desea ejecutar: "))
    if seleccion == 1:
        import ejercicios.ejer1
    elif seleccion == 2:
        from ejercicios.ejer2 import Cadena
        cadena = input("Introduzca una frase: ")
        lista = list(cadena)
        print(lista)
        print(Cadena.comprobacion(lista))
    elif seleccion == 3:
        from ejercicios.ejer3 import lista010, lista100, listapar20, listaimpar20, lista5
        print(lista010(0, []))
        print(lista100(-10, []))
        print(listapar20(0, []))
        print(listaimpar20(-20, []))
        print(lista5(0, []))
    elif seleccion == 4:
        from ejercicios.tabla import Tabla 
        Tabla.generador3()
        