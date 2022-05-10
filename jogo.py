import time
from colorama import Fore
import scriptsbase as sb    
from database import DADOS, EARTH_RADIUS, pais_h, setup, pais_sorte, paises

raio = EARTH_RADIUS
jogar = 's'
print()
print('=D==E==S==S==O==F==/==D==E==S==S==O==F==|  '+Fore.LIGHTGREEN_EX+'Bem-Vindo ao EP2 - Jogo dos Países  '+Fore.RESET+'|==D==E==S==S==O==F==/==D==E==S==S==O==F==')
print()
print(Fore.LIGHTMAGENTA_EX+'Feito para nosso querido professor, qual era o nome dele mesmo?...\n'+Fore.RESET+'\nComandos:')
print('     dicas       - Acesso ao mercado de dicas ($)')
print('     desisto     - Desistir da rodada (⌣̩̩́  _⌣̩̩̀ )')
print('     inventario  - Mostra suas tentativas e dicas compradas\n')
print('Você tem'+Fore.LIGHTCYAN_EX+' 20 '+ Fore.RESET +'tentativas!\n\n')

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
            print('Parabéns, você perdeu! O país era '+Fore.LIGHTCYAN_EX+'{}'+ Fore.RESET +':)'.format(pais_sorte))
            break
        guess = input("Adivinhe um país: ").lower()

        # Vitória
        if guess == pais_sorte:
            print(Fore.LIGHTCYAN_EX+'\nVocê venceu!!!\n'+Fore.LIGHTGREEN_EX+'\nDica: '+Fore.RESET+'quando for adivinhar um país, digite humberto\n')
            break

        # Desistência
        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada?"+ Fore.LIGHTGREEN_EX+" [s/n] "+Fore.RESET).lower()
            if certeza == 's':
                print('Você é fraco. O país era '+Fore.LIGHTCYAN_EX+'{0}'.format(pais_sorte) + Fore.RESET)
                t = 0
                break
        
        # Interaction
        elif guess == pais_h:
            resultado = setup(10,10,0,0)
            if resultado == 'vitoria':
                print("\nVocê derrotou o "+ Fore.LIGHTRED_EX +"Deus do python"+ Fore.RESET +"... essa é sua recompensa:\n")
                time.sleep(1)
                print("O país sorteado era:"+ Fore.LIGHTMAGENTA_EX +"{0}\n".format(pais_sorte) + Fore.RESET)
                time.sleep(1)
                print("Final secreto desbloqueado!\n")
                time.sleep(1)
                
            else:
                print("Você foi DEBUGADO!\n")
                time.sleep(1)
                print("Não lhe resta mais nada, além do amargo gosto da derrota...\n")
                time.sleep(2)
                print("Desistir seria a opção mais sensata...\n")
                time.sleep(1)
                print("Mas você não ira desistir, irá?\n")
                break

        # Inventario
        elif guess == 'inventario':
            sb.checainventario(tent_paises,dicas)

        # Menu Dicas
        elif guess == 'dicas' or guess == 'dica':
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
                print('\n\nJá tentou esse país, perdeu ponto por ser '+Fore.LIGHTRED_EX+'boboca!\n\n'+Fore.RESET)
        
        if guess != 'inventario' and guess != pais_h:
            sb.printa_status(tent_paises,dicas,t)
    
    jogar = input('Quer jogar novamente?'+ Fore.LIGHTGREEN_EX+'[s/n]\n'+Fore.RESET).lower()
    if jogar == 's':
        print('Um país foi sorteado, Boa sorte!')
            
print('falou!')
