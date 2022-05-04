import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)
tent_paises = {}
jogar = 's'

while jogar == 's':
    tentativas = 20
    pais_sorte = sb.sorteia_pais(paises)
    while tentativas > 0:
        guess = input("Adivinhe um país: ").lower()
        if guess == pais_sorte:
            print('Você venceu!!!')
            break

        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada? [s/n] ").lower()
            if certeza == 's':
                print('Você é fraco. O país era {0}'.format(pais_sorte))
                tentativas = 0
                break
        
        elif guess == 'dicas':
            print('dicas')
            
        elif guess not in paises:
            print("País desconhecido, tente outro...")
        
        else:
            print("Sim")
            tentativas -= 1
            tent_paises[guess] = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            print(pais_sorte, tent_paises)
            print('Você tem : {} tentativas sobrando!'.format(tentativas))
    jogar = input('Quer jogar novamente? [s/n] ').lower()
print('falou!')
