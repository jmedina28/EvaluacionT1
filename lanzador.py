

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
        from ejercicios.ejer3 import Listas
        opcion = 1
        for i in range(5):
            print("Opción", opcion, ":", Listas.generador2(opcion))
            opcion += 1
    elif seleccion == 4:
        from ejercicios.tabla import Tabla 
        Tabla.generador3()
        