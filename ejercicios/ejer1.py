import random

matriz = []
fila = 0
dimensiones = int(input("Introduzca el número de filas que desea que tenga su matriz ix4: "))
def generador1(dim):
   if dim == 0:
     return
   else:
     matriz.append([])
     generador1(dim-1)
f = 1
def elementouser(matriz,f):
    if len(matriz) == 0:
        return
    else:
        print("Introduzca los elementos de la fila" , f)
        for i in range(3):
            matriz[fila].append(int(input("Introduzca un elemento: ")))
        elementouser(matriz[1:],f+1)
def elementorandom(matriz,f):
    if len(matriz) == 0:
        return
    else:
        for i in range(3):
            matriz[fila].append(random.randint(0,10))
        elementorandom(matriz[1:],f+1)

def suma(matriz):
    if len(matriz) == 0:
        return
    else:
        matriz[fila].append(matriz[fila][0] + matriz[fila][1] + matriz[fila][2])
        suma(matriz[1:])
generador1(dimensiones)
modo = int(input("Introduzca 1 si desea introducir los elementos de la matriz o 2 si desea que sean aleatorios: "))
if modo == 1:
    elementouser(matriz,f)
elif modo == 2:
    elementorandom(matriz,f)
suma(matriz)
print(matriz)