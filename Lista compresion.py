'''boca = [x for x in range(30) if x%2 == 1 ]
print(boca)
'''
a = input("Ingrese una palabra: ")
'''

def challenge(b):
    lista = []
    lista[:0] = b
    reversed(lista)
    if lista != None:
        for x in lista:
            print(x)
    else:
        challenge(b)

challenge(a)
'''

def challenge2(string):
    lista = []
    lista[:0] = string
    diccio = {lista[x]: lista.count(lista[x]) for x in range(0, len(lista), 2)}
    for o in diccio:
        print({o: diccio[o]})

challenge2(a)