import scriptsbase as sb
from database import DADOS, EARTH_RADIUS

raio = EARTH_RADIUS
paises = sb.normaliza(DADOS)
tent_paises = {}
jogar = 's'
dicas = {}

while jogar == 's':
    t = 20
    pais_sorte = sb.sorteia_pais(paises)
    while t > 0:
        if t == 0:
            print('Parabéns, você perdeu! O país era {}'.format(pais_sorte))
            break
        guess = input("Adivinhe um país: ").lower()
        print('')
        # Vitória
        if guess == pais_sorte:
            print('Você venceu!!!')
            print('')
            break

        # Desistência
        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada? [s/n] ").lower()
            if certeza == 's':
                print('Você é fraco. O país era {0}'.format(pais_sorte))
                t = 0
                break
        
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

            print('0. Cancelar')
            print('')
            disponivel = '|'.join(disp)

            while True:
                tip = input('Escolha sua opção [{}]: '.format(disponivel))
                if tip not in disp:
                    print('Opção Inválida!')
                    print('')

                # The end is near...     
                elif tip == '6' and 'The end is near (Digite: Humberto)' not in dicas: 
                    dicas['The end is near! '] = '(Digite: Humberto)'
                    t -= 19
                    break

                # Continente
                elif tip == '5' and 'Continente' not in dicas:
                    dicas['Continente: '] = paises[pais_sorte]['continente']
                    t -= 7
                    break

                # População
                elif tip == '4'and 'População: ' not in dicas:
                    dicas['População: '] = paises[pais_sorte]['populacao'] + ' habitantes'
                    t -= 5
                    break

                # Área
                elif tip == '3' and "Área: " not in dicas: 
                    dicas["Área: "] =  '{} km2'.format(paises[pais_sorte]['area'])
                    t -= 6
                    break

                # Letra da Capital
                elif tip == '2':
                    t -= 3
                    break

                # Cor da Bandeira
                elif tip == '1':
                    t -= 4
                    break

                # Cancelar
                elif tip == '0':
                    break
            print('Tentativas Restantes: {}'.format(t))
            print('')

        # Pais digitado not in paises    
        elif guess not in paises:
            print("País desconhecido, tente outro...")
            print('')
        
        # Pais in paises
        else:
            t -= 1
            tent_paises[guess] = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            if t != 0:
                print('Você tem : {} tentativas sobrando!'.format(t))
            print('')


        print("Distâncias:")
        for i in tent_paises:
            print('     {} --> {:.2f} km'.format(i, tent_paises[i]))
        print('')
        if dicas != {}:
            print("Dicas:")
            for i in dicas:
                print('     - {}{}'.format(i, dicas[i]))
                print('')
        
    jogar = input('Quer jogar novamente? [s/n] ').lower()
print('falou!')
