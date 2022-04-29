def normaliza(dic):
    normal = {}
    for continente, paises in dic.items():
        for pais in paises.keys():
            info = dic[continente][pais]
            info['continente'] = continente
            normal[pais] = info
    return normal