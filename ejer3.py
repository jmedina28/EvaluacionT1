
def generador(opcion):
  lista = []
  if opcion == 1:
    for i in range(11):
      lista.append(i)
  elif opcion  == 2:
    for i in range(-10,1):
      lista.append(i)
  elif opcion == 3:
    for i in range(-20,1):
      if i % 2 != 0:
        lista.append(i)
  return(lista)
print(generador(3))
