
def lista010(n, lista):
  lista.append(n)
  if n < 10:
    n += 1
    lista010(n, lista)
    return lista

def lista100(n, lista):
  lista.append(n)
  if n<0:
    n += 1
    lista100(n,lista)
    return lista

def listapar20(n, lista):
  lista.append(n)
  if n<20:
    n +=2
    listapar20(n,lista)
    return lista


def listaimpar20(n, lista):
  lista.append(n)
  if n<0:
    n +=2
    listaimpar20(n,lista)
    return lista

def lista5(n,lista):
  lista.append(n)
  if n<50:
    n +=5
    lista5(n,lista)
    return lista
