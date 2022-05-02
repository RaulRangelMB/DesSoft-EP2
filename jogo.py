import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

tentativas = 20
raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)

while tentativas > 0:
    guess = input("adivinhe um país: ").lower()
    if guess not in paises:
        print("País desconhecido, tente outro...")
        
    else:
        print("Sim")
        tentativas -= 1
        print(tentativas)

