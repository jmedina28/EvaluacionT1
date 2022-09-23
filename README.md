<h1 align="center">Evaluación del Tema 1</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EvaluacionT1) quedan resueltos los ejercicios de evaluación del tema 1.
***

El código empleado para resolver el ejercicio 1 es el siguiente:

```python
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
```

El código empleado para resolver el ejercicio 2 es el siguiente:

```python
class Cadena:
  def comprobacion(lista):
    if len(lista) >= 3 and len(lista) < 10:
      return True
    else:
      return False
    
```

El código empleado para resolver el ejercicio 3 es el siguiente:

```python

def listas(n, lista, j,lim):
  lista.append(n)
  if n<lim:
    n += j
    listas(n,lista,j,lim)
    return lista

```

El código empleado para resolver el ejercicio 4 es el siguiente:

```python

class Tabla:
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
```
