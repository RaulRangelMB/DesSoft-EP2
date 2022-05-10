import time
import scriptsbase as sb    
from database import DADOS, EARTH_RADIUS, pais_h, setup, pais_sorte, paises

raio = EARTH_RADIUS
jogar = 's'

print('\nBem-Vindo ao EP2 - Jogo dos Países\nFeito para nosso querido professor, qual era o nome dele mesmo?...\n\nComandos:')
print('     dicas       - Acesso ao mercado de dicas ($)')
print('     desisto     - Desistir da rodada (⌣̩̩́  _⌣̩̩̀ )')
print('     inventario  - Mostra suas tentativas e dicas compradas')

while jogar == 's':
    t = 20

    tent_paises = []    # Países Digitados
    dicas = {}          # Dicas comprada com sua informação

    cap = paises[pais_sorte]['capital'].strip()
    l_cap = list(cap) 

    l_cap_tent = []          # Letra da Capital
    c_band_tent = []         # Cores da Bandeira

    while t >= 0:
        # Derrota
        if t == 0:
            print('Parabéns, você perdeu! O país era {} :)'.format(pais_sorte))
            break

        guess = input("Adivinhe um país: ").lower()

        # Vitória
        if guess == pais_sorte:
            print('Você venceu!!!\nDica: quando for adivinhar um país, digite humberto')
            break

        # Desistência
        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada? [s/n] ").lower()
            if certeza == 's':
                print('Você é fraco. O país era {0}'.format(pais_sorte))
                t = 0
                break
        
        # Interaction
        elif guess == pais_h:
            resultado = setup(10,10,0)
            if resultado == 'vitoria':
                print("Você derrotou o Deus do python... essa é sua recompensa:")
                time.sleep(1)
                print("O país sorteado era: {0}".format(pais_sorte))
                time.sleep(1)
                print("Fim secreto desbloqueado!")
                time.sleep(1)
                print("Obrigado por jogar!")
                time.sleep(1)
                break
            else:
                print("Você foi derrotado...")
                time.sleep(1)
                print("Não lhe resta mais nada...")
                time.sleep(1)
                print("Além do amargo gosto da derrota...")
                time.sleep(1)
                break

        # Inventario
        elif guess == 'inventario':
            sb.checainventario(paises,dicas)

        # Menu Dicas
        elif guess == 'dicas':
            t = sb.menudicas(paises,pais_sorte,dicas,t,l_cap_tent,c_band_tent)

        # Pais digitado not in paises    
        elif guess not in paises:
            print("País desconhecido, tente outro...")
        
        # Pais in paises
        else:
            t -= 1
            d = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            if [guess, d] not in tent_paises:
                tent_paises = sb.adiciona_em_ordem(guess, d, tent_paises)
            else:
                print('\n\nJá tentou esse país, perdeu ponto por ser boboca!\n\n')
        
        if guess != 'inventario' and guess != 'humberto':
            sb.printa_status(tent_paises,dicas,t)
    
    jogar = input('Quer jogar novamente? [s/n]\n').lower()
    if jogar == 's':
        print('Um país foi sorteado, Boa sorte!')
        print('Você tem 20 tentativas!')
            
print('falou!')
