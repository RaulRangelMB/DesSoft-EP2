def esta_na_lista(pais, lista):
    for info in lista:
        if pais in info:
            return True
    return False