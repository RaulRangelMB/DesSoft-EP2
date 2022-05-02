import random
import math

def adiciona_em_ordem(pais, d, lista):
    n = 0
    for i in range(len(lista)):
        if d < lista[i][1]:
            break
        n += 1
    lista.insert(n, [pais, d])
    return lista

def sorteia_pais(paises):
    chaves = list(paises.keys())
    return random.choice(chaves)

def esta_na_lista(pais, lista):
    for info in lista:
        if pais in info:
            return True
    return False

def normaliza(dic):
    normal = {}
    for continente, paises in dic.items():
        for pais in paises.keys():
            info = dic[continente][pais]
            info['continente'] = continente
            normal[pais] = info
    return normal

def sorteia_pais(paises):
    chaves = list(paises.keys())
    return random.choice(chaves)

def sorteia_letra(p, rest):
    ce = ['.', ',', '-', ';', ' ']
    ra = ''
    for ver in p:
        if ver.lower() not in rest and ver not in ce:
            if ver.upper() not in rest:
                ra += ver.lower()
    if len(ra) == False:
        return ra
    else:
        return random.choice(ra)

def haversine(r, p1,l1,p2,l2):
    aux1 = (math.sin( math.radians((p2-p1)/2 )))**2
    aux2 = math.cos(math.radians(p1))*math.cos(math.radians(p2))
    aux3 = (math.sin( math.radians((l2-l1)/2 )))**2
    d = 2*r*math.asin( (aux1 + aux2*aux3)**(1/2) )
    return d