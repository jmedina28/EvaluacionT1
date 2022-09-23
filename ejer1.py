import random

matriz = []
fila = 0
dimensiones = int(input("Introduzca el número de filas que desea que tenga su matriz ix4: "))


def generador(dim):
  
  for i in range(dim):
    matriz.append([])
    for j in range(3):
      matriz[i].append(random.randint(0,10))
   
    
generador(dimensiones)
print(matriz)