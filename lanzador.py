

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
        from ejercicios.ejer3 import listas
        print(listas(0,[],1,10))
        print(listas(-10,[],1,0))
        print(listas(0,[],2,20))
        print(listas(-19,[],2,-1))
        print(listas(0,[],5,50))
    elif seleccion == 4:
        from ejercicios.tabla import Tabla 
        Tabla.generador3()
        