import time
from colorama import Fore
import scriptsbase as sb    
from database import EARTH_RADIUS, pais_h, setup, paises

raio = EARTH_RADIUS
jogar = 's'

print('=D==E==S==S==O==F==/==D==E==S==S==O==F==|  '+ sb.cores('Bem-Vindo ao EP2 - Jogo dos Países  ', 'lgreen')+'|==D==E==S==S==O==F==/==D==E==S==S==O==F==')
print()
print(sb.cores('Feito para nosso querido professor, qual era o nome dele mesmo?...\n','lmagenta')+'\nComandos:')
print('     '+ sb.cores('dicas', "lyellow")+'       - Acesso ao mercado de dicas ($)')
print('     '+ sb.cores('desisto','lred')+'     - Desistir da rodada (⌣̩̩́  _⌣̩̩̀ )')
print('     '+ sb.cores('inventario',"lgreen")+'  - Mostra suas tentativas e dicas compradas\n')
print('Você tem'+ sb.cores(' 20 ',"lcyan")+'tentativas!')

# Loop para quando o jogador ainda quer jogar
while jogar == 's':

    # Reiniciando as tentativas e sorteando um novo país
    t = 20
    pais_sorte = sb.sorteia_pais(paises)

    print('\nUm país foi sorteado, Boa sorte!')

    tent_paises = []    # Países Digitados
    dicas = {}          # Dicas comprada com sua informação

    cap = paises[pais_sorte]['capital'].strip()
    l_cap = list(cap) 

    l_cap_tent = []          # Letra da Capital
    c_band_tent = []         # Cores da Bandeira

    # Loop para quando o jogador ainda tem tentativas
    while t >= 0:
        # Derrota
        if t == 0:
            print('Acabaram suas tentativas! O país era '+ sb.cores('{}'.format(pais_sorte), 'lcyan')+' :)')
            break
        guess = input("Adivinhe um país: ").lower()

        # Vitória
        if guess == pais_sorte:
            print(Fore.LIGHTCYAN_EX+'\nVocê venceu!!!')
            time.sleep(1)
            print(sb.cores('\nDica: ',"lgreen")+'quando for adivinhar um país, digite humberto\n')
            break

        # Desistência
        elif guess == 'desisto':
            certeza = input("Tem certeza que quer desistir dessa rodada?"+ sb.cores(" [s/n]\n", "lgreen")).lower()
            if certeza == 's':
                print('Você é fraco. O país era '+ sb.cores('{0}\n'.format(pais_sorte),"lcyan"))
                t = 0
                break

        
        # Interaction
        elif guess == pais_h:
            t = 1
            resultado = setup(5,10,2,0)
            if resultado == 'vitoria':
                print("\nVocê derrotou o "+ sb.cores("Deus do python","lred")+"... essa é sua recompensa:\n")
                time.sleep(2)
                print("O país sorteado é "+ sb.cores("{0}\n".format(pais_sorte),"lmagenta"))
                time.sleep(2)
                print("**Final secreto desbloqueado!**\n")
                time.sleep(1)
                print('\nVocê tem '+ sb.cor_tentativa(t)+' tentativa!\n\n')
                
            else:
                print("Você foi "+ sb.cores("DEBUGADO!\n",'lred'))
                time.sleep(1)
                print("Não lhe resta mais nada, além do amargo gosto da "+ sb.cores("derrota...\n","lred"))
                time.sleep(2)
                print("Desistir seria a opção mais sensata...\n")
                time.sleep(1)
                print(sb.cores("Mas você não ira desistir, irá?\n","lyellow"))
                break

        # Inventario
        elif guess == 'inventario':
            sb.checainventario(tent_paises,dicas)

        # Menu Dicas
        elif guess == 'dicas' or guess == 'dica':
            t = sb.menudicas(paises,pais_sorte,dicas,t,l_cap_tent,c_band_tent)

        # Se o ais digitado nao estiver na lista de paises    
        elif guess not in paises:
            print("País desconhecido, tente outro...")
        
        # Se o ais digitado estiver na lista de paises 
        else:
            t -= 1
            d = sb.haversine(raio, paises[guess]['geo']['latitude'], paises[guess]['geo']['longitude'], paises[pais_sorte]['geo']['latitude'], paises[pais_sorte]['geo']['longitude'])
            if [guess, d] not in tent_paises:
                tent_paises = sb.adiciona_em_ordem(guess, d, tent_paises)
            else:
                print("\n\nJá colocou esse país, seu "+sb.cores("boboca! \n","lred"))
                t+=1
        
        if guess != 'inventario' and guess != pais_h:
            sb.printa_status(tent_paises,dicas,t)
    
    # Perguntar se o jogador quer continuar a jogar
    while True:
        jogar = input('Quer jogar novamente?'+ sb.cores(' [s/n]: \n',"lgreen")).lower()
        if jogar == 's' or jogar == 'n':
            break
        else:
            print('(?)')
            time.sleep(1)
            print("\nIsso é um "+sb.cores("sim?","lgreen") + " Isso é um "+sb.cores("não?","lred")+" Não to entendendo...\n")
            
print('Obrigado por jogar!')
