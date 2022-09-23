
def generador3():
    
    filas = int(input("Introduzca el número de filas que desea que tenga su tabla: "))
    columnas = int(input("Introduzca el número de columnas que desea que tenga su tabla: "))

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print("Filas o columnas incorrectas")
    else:
        for i in range(filas):
            print("")
            for j in range(columnas):
                print(" * ", end='')