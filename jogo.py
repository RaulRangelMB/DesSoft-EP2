import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)
jogar = 's'

print('\nBem-Vindo ao EP2 - Jogo dos Países\n\nComandos:')
print('     dicas       - Acesso ao mercado de dicas ($)')
print('     desisto     - Desistir da rodada (⌣̩̩́  _⌣̩̩̀ )')
print('     inventario  - Mostra suas tentativas e dicas compradas')

while jogar == 's':
    t = 20
    pais_sorte = sb.sorteia_pais(paises)

    tent_paises = []    # Países Digitados
    dicas = {}          # Dicas comprada com sua informação

    cap = paises[pais_sorte]['capital'].strip()
    l_cap = list(cap)

    # c_band = 

    l_cap_tent = []          # Letra da Capital
    c_band_tent = []         # Cores da Bandeira

    while t > 0:
        # Derrota
        if t == 0:
            print('Parabéns, você perdeu! O país era {}'.format(pais_sorte))
            break

        guess = input("Adivinhe um país: ").lower()

        # Vitória
        if guess == pais_sorte:
            print('Você venceu!!!\n')
            break

        # Desistência
        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada? [s/n] ").lower()
            if certeza == 's':
                print('Você é fraco. O país era {0}'.format(pais_sorte))
                t = 0
                break
        
        # Fear
        elif guess == 'humberto':
            print('\noh no\n')

        # Inventario
        elif guess == 'inventario':
            print('\nDistâncias: ')
            for i in tent_paises:
                print('     {} --> {:.2f} km'.format(i, tent_paises[i]))
            print('Dicas: ')
            for i in dicas:
                print('     - {}{}\n'.format(i, dicas[i]))
            print()

        
        # Menu Dicas
        elif guess == 'dicas':
            disp = ['0']
            print('Mercado de Dicas:  Recomendação: Dica 6 (Recomeçar caso nescessário)')
            if t > 4:
                print('1. Cor da Bandeira    - custa 4 tentativas')
                disp.append('1')
            if t > 3:
                print('2. Letra da Capital   - custa 3 tentativas')
                disp.append('2')
            if t > 6 and "Área: " not in dicas:
                print('3. Área               - custa 6 tentativas')
                disp.append('3')
            if t > 5 and 'População: ' not in dicas:
                print('4. População          - custa 5 tentativas')
                disp.append('4')
            if t > 7 and 'Continente: ' not in dicas:
                print('5. Continente         - custa 7 tentativas')
                disp.append('5')
            if t == 20 and 'The end is near (Digite: Humberto)' not in dicas:
                print('6. Você está pronto?  - custa 19 tentativas')
                disp.append('6')

            print('0. Cancelar\n')
            disponivel = '|'.join(disp)

            while True:
                tip = input('Escolha sua opção [{}]: '.format(disponivel))
                if tip not in disp:
                    print('Opção Inválida!\n')

                # The end is near...  (Never Done!)  ( º-º)
                elif tip == '6' and 'The end is near (Digite: Humberto)' not in dicas: 
                    dicas['The end is near! '] = '(Digite: Humberto)'
                    t -= 19
                    break

                # Continente (Done)
                elif tip == '5' and 'Continente' not in dicas:
                    dicas['Continente: '] = paises[pais_sorte]['continente']
                    t -= 7
                    break

                # População (Done)
                elif tip == '4'and 'População: ' not in dicas:
                    dicas['População: '] = paises[pais_sorte]['populacao'] + ' habitantes'
                    t -= 5
                    break

                # Área (Done)
                elif tip == '3' and "Área: " not in dicas: 
                    dicas["Área: "] =  '{} km2'.format(paises[pais_sorte]['area'])
                    t -= 6
                    break

                # Letra da Capital
                #===============================================================================================================================
                # Comment: Verificar se tem alguma letra possível na capital pra ser dada ao player, senão devolver que não há mais letras
                #===============================================================================================================================
                elif tip == '2':
                    while True:
                        letra = sb.sorteia_letra(pais_sorte, [])
                        if letra not in l_cap_tent:
                            l_cap_tent.append( letra )
                            break
                    dicas["Letras da Capital: "] = l_cap_tent
                    t -= 3
                    break

                # Cor da Bandeira
                elif tip == '1':
                    t -= 4
                    break

                # Cancelar (Done)
                elif tip == '0':
                    break
            print('Tentativas Restantes: {}\n'.format(t))

        # Pais digitado not in paises    
        elif guess not in paises:
            print("País desconhecido, tente outro...\n\n")
        
        # Pais in paises
        else:
            t -= 1
            d = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            if [guess, d] not in tent_paises:
                tent_paises = sb.adiciona_em_ordem(guess, d, tent_paises)
            else:
                print('\n\nJá tentou esse país, perdeu ponto por ser boboca!\n\n')

            if t != 0:
                print('Você tem : {} tentativas sobrando!\n'.format(t))
        

        if guess != 'inventario' and guess != 'humberto':
            if tent_paises != []:
                print("Distâncias:")
                for i in tent_paises:
                    print('     {} --> {:.2f} km'.format(i[0], i[1]))
            if dicas != {}:
                print("Dicas:")
                for i in dicas:
                    print('     - {}{}\n'.format(i, dicas[i]))
        
    jogar = input('Quer jogar novamente? [s/n]\n').lower()
print('falou!')
