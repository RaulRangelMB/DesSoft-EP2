from ScriptsBase import normalizadatabase
from database import DADOS, EARTH_RADIUS

tentativas = 20
raio = EARTH_RADIUS
paises = normalizadatabase.normaliza(DADOS)

while tentativas > 0:
    guess = input("adivinhe um país: ")
    if guess not in paises:
        print("nao")
    else:
        print("sim")
    tentativas -= 1