import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

tentativas = 20
raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)
pais_sorte = sb.sorteia_pais(paises)
tent_paises = {}

while tentativas > 0:
    guess = input("adivinhe um país: ").lower()
    if guess == 'dicas':
        print('dicas')
        
    elif guess not in paises:
        print("País desconhecido, tente outro...")
    
    else:
        print("Sim")
        tentativas -= 1
        tent_paises[guess] = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
        print(pais_sorte, tent_paises)
        print('Você tem : {} tentativas sobrando!'.format(tentativas))

