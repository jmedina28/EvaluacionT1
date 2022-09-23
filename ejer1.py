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

generador1(dimensiones)

def elemento(matriz):
    if len(matriz) == 0:
        return
    else:
        for i in range(3):
            matriz[fila].append(random.randint(0,10))
        elemento(matriz[1:])
elemento(matriz)
print(matriz)