lista10 = [2, 5, 8, 1, 6, 9, 69, 84, 14, 0]
'''
def max(lista):
  posicion = 1
  maximo = lista[0]
  contador = 0
  while contador <= len(lista) and posicion <= 9:
    if maximo < lista[posicion]:
      maximo = lista[posicion]
    else:
      posicion = posicion + 1
      contador = contador + 1
  print(f"El máximo de tu lista es {maximo}")


max(lista10)
'''

def getmax(lista):
  max = 0
  for x in lista:
    if x >= max:
      max = x
  print(max)

getmax(lista10)