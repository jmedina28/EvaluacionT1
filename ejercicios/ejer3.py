
def listas(n, lista, j,lim):
  lista.append(n)
  if n<lim:
    n += j
    listas(n,lista,j,lim)
    return lista