cadena = input("Introduzca una frase: ")

lista = list(cadena)
print(lista)

def comprobacion(lista):
  if len(lista) >= 3 and len(lista) < 10:
    return True
  else:
    return False
    
print(comprobacion(lista))