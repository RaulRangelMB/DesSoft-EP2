import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)
tent_paises = {}
jogar = 's'

while jogar == 's':
    t = 20
    pais_sorte = sb.sorteia_pais(paises)
    while t > 0:
        guess = input("Adivinhe um país: ").lower()
        if guess == pais_sorte:
            print('Você venceu!!!')
            break

        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada? [s/n] ").lower()
            if certeza == 's':
                print('Você é fraco. O país era {0}'.format(pais_sorte))
                t = 0
                break
        
        elif guess == 'dicas':
            disp = ['0']
            print('Mercado de Dicas:  Recomendação: Dica 6 (Recomeçar caso nescessário)')
            if t > 4:
                print('1. Cor da Bandeira    - custa 4 tentativas')
                disp.append('1')
            if t > 3:
                print('2. Letra da Capital   - custa 3 tentativas')
                disp.append('2')
            if t > 6:
                print('3. Área               - custa 6 tentativas')
                disp.append('3')
            if t > 5:
                print('4. População          - custa 5 tentativas')
                disp.append('4')
            if t > 7:
                print('5. Continente         - custa 7 tentativas')
                disp.append('5')
            if t == 20:
                print('6. Você está pronto?  - custa 19 tentativas')
                disp.append('6')
            print('0. Cancelar')
            disponivel = '|'.join(disp)
            while True:
                tip = input('Escolha sua opção [{}]: '.format(disponivel))
                if tip not in disp:
                    print('Opção Inválida!')
                elif tip == '6': # The end is near...
                    print('Dica: digite Humberto...')
                    t -= 19
                    break
                elif tip == '5': # Continente
                    print('Continente')
                    t -= 7
                    break
                elif tip == '4': # População
                    print('População')
                    t -= 5
                    break
                elif tip == '3': # 
                    print('Área')
                    t -= 6
                    break
                elif tip == '2':
                    print('Letra da capital')
                    t -= 3
                    break
                elif tip == '1':
                    print('Cor da Bandeira')
                    t -= 4
                    break
                elif tip == '0':
                    break
            print('Tentativas Restantes: {}'.format(t))

        elif guess not in paises:
            print("País desconhecido, tente outro...")
        
        else:
            print("Sim")
            t -= 1
            tent_paises[guess] = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            print(pais_sorte, '{} --> {:.2f} km'.format(guess, tent_paises[guess]))
            print('Você tem : {} tentativas sobrando!'.format(t))
    jogar = input('Quer jogar novamente? [s/n] ').lower()
print('falou!')
