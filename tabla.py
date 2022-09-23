
tabla = []
def generador3(i,j):
    for n in range(i):
        tabla.append([])
        for z in range(j):
            tabla[n].append(" ")
generador3(4,8)
print(tabla)
