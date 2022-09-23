class Listas:
  def generador2(opcion):
    lista = []
    if opcion == 1:
      for i in range(11):
        lista.append(i)
    elif opcion  == 2:
      for i in range(-10,1):
        lista.append(i)
    elif opcion == 3:
      for i in range(0,21,2):
        lista.append(i)
    elif opcion == 4:
      for i in range(-20,1):
        if i % 2 != 0:
          lista.append(i)
    elif opcion == 5:
      for i in range(0,51,5):
        lista.append(i)
    return lista

