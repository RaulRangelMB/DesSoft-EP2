def adiciona_em_ordem(pais, d, lista):
    n = 0
    for i in range(len(lista)):
        if d < lista[i][1]:
            break
        n += 1
    lista.insert(n, [pais, d])
    return lista