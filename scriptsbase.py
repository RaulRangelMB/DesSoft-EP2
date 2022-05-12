import random
import math
from colorama import Fore

def adiciona_em_ordem(pais, d, lista):
    n = 0
    for i in range(len(lista)):
        if d < lista[i][1]:
            break
        n += 1
    lista.insert(n, [pais, d])
    return lista

def sorteia_pais(paises):
    chaves = list(paises.keys())
    return random.choice(chaves)

def esta_na_lista(pais, lista):
    for info in lista:
        if pais in info:
            return True
    return False

def normaliza(dic):
    normal = {}
    for continente, paises in dic.items():
        for pais in paises.keys():
            info = dic[continente][pais]
            info['continente'] = continente
            normal[pais] = info
    return normal

def sorteia_pais(paises):
    chaves = list(paises.keys())
    return random.choice(chaves)

def sorteia_letra(p, rest):
    ce = ['.', ',', '-', ';', ' ']
    ra = ''
    for ver in p:
        if ver.lower() not in rest and ver not in ce:
            if ver.upper() not in rest:
                ra += ver.lower()
    if len(ra) == False:
        return ra
    else:
        return random.choice(ra)

def cor_da_bandeira(cores,cores_atuais):
    while True:
        cor = random.choice(list(cores.keys()))
        if cores[cor] != 0 and cor != "outras" and cor not in cores_atuais:
            return cor

def haversine(r, p1,l1,p2,l2):
    aux1 = (math.sin( math.radians((p2-p1)/2 )))**2
    aux2 = math.cos(math.radians(p1))*math.cos(math.radians(p2))
    aux3 = (math.sin( math.radians((l2-l1)/2 )))**2
    d = 2*r*math.asin( (aux1 + aux2*aux3)**(1/2) )
    return d

def menudicas(listapaises,pais_sorteado,dicasusadas,tentativas,letrascap,coresbandeira):
    disp = ['0']
    print('\n=$==$==$==$==$==$==$==$==$==$==$==$==$==$'+Fore.LIGHTYELLOW_EX+'  Mercado de Dicas:  '+Fore.RESET+'$==$==$==$==$==$==$==$==$==$==$==$==$==$=')
    print(Fore.LIGHTGREEN_EX+'Recomendação do dia: Dica 6 (Recomeçar caso nescessário)\n'+Fore.RESET)
    if tentativas > 4:
        print('1. Cor da Bandeira    - custa'+Fore.LIGHTYELLOW_EX+' 4 '+Fore.RESET+'tentativas')
        disp.append('1')
    if tentativas > 3:
        print('2. Letra da Capital   - custa'+Fore.LIGHTYELLOW_EX+' 3 '+Fore.RESET+'tentativas')
        disp.append('2')
    if tentativas > 6 and "Área: " not in dicasusadas:
        print('3. Área               - custa '+Fore.LIGHTYELLOW_EX+'6 '+Fore.RESET+'tentativas')
        disp.append('3')
    if tentativas > 5 and 'População: ' not in dicasusadas:
        print('4. População          - custa'+Fore.LIGHTYELLOW_EX+' 5 '+Fore.RESET+'tentativas')
        disp.append('4')
    if tentativas > 7 and 'Continente: ' not in dicasusadas:
        print('5. Continente         - custa '+Fore.LIGHTYELLOW_EX+'7 '+Fore.RESET+'tentativas')
        disp.append('5')
    if tentativas == 20 and 'The end is near (Digite: Humberto)' not in dicasusadas:
        print('6. '+Fore.LIGHTCYAN_EX+'Você está pronto?  - custa '+Fore.LIGHTYELLOW_EX+'19 '+Fore.LIGHTCYAN_EX+'tentativas'+Fore.RESET)
        disp.append('6')

    print('0. Cancelar\n')
    disponivel = '|'.join(disp)

    while True:
        tip = input('Escolha sua opção'+Fore.LIGHTYELLOW_EX+' [{}]: '.format(disponivel)+Fore.RESET)
        if tip not in disp:
            print('Opção Inválida!\n')

        # The end is near...  (Never Done!)  ( º-º)
        elif tip == '6' and 'The end is near (Digite: Humberto)' not in dicasusadas: 
            dicasusadas['The end is near! '] = '(Digite: Humberto)'
            tentativas -= 19
            break

        # Continente (Done)
        elif tip == '5' and 'Continente' not in dicasusadas:
            dicasusadas['Continente: '] = listapaises[pais_sorteado]['continente']
            tentativas -= 7
            break

        # População (Done)
        elif tip == '4'and 'População: ' not in dicasusadas:
            dicasusadas['População: '] = str(listapaises[pais_sorteado]['populacao']) + ' habitantes'
            tentativas -= 5
            break

        # Área (Done)
        elif tip == '3' and "Área: " not in dicasusadas: 
            dicasusadas["Área: "] =  '{} km²'.format(listapaises[pais_sorteado]['area'])
            tentativas -= 6
            break

        elif tip == '2':
            while True:
                letra = sorteia_letra(pais_sorteado, letrascap)
                if letra not in letrascap:
                    letrascap.append( letra )
                    break
            
            dicasusadas["Letras da Capital: "] = ''
            for letra in letrascap:
                if dicasusadas["Letras da Capital: "] == '':
                    dicasusadas["Letras da Capital: "] += letra
                else:
                    dicasusadas["Letras da Capital: "] += ', {}'.format(letra)
            tentativas -= 3
            break

        # Cor da Bandeira
        elif tip == '1':
            while True:
                cor = cor_da_bandeira(listapaises[pais_sorteado]["bandeira"], coresbandeira)
                if cor not in coresbandeira:
                    coresbandeira.append(cor)
                    break
                
            dicasusadas["Cores da Bandeira: "] = ''
            for cor in coresbandeira:
                if dicasusadas["Cores da Bandeira: "] == '':
                    dicasusadas["Cores da Bandeira: "] += cor
                else:
                    dicasusadas["Cores da Bandeira: "] += ', {}'.format(cor)
            tentativas -= 4
            break

        # Cancelar (Done)
        elif tip == '0':
            break
    # print('Tentativas Restantes: {}'.format(tentativas))
    return tentativas

def cor_tentativa(tentativas):
    if tentativas > 11:
        return Fore.LIGHTCYAN_EX + '{}'.format(tentativas) + Fore.RESET
    elif tentativas > 6:
        return Fore.LIGHTYELLOW_EX + '{}'.format(tentativas) + Fore.RESET
    return Fore.LIGHTRED_EX + '{}'.format(tentativas) + Fore.RESET

def checainventario(paises,dicasusadas):
        print('\n=D==E==S==S==O==F==/==D==E==S==S==O==F==|'+Fore.LIGHTGREEN_EX+'  Inventário:  '+Fore.RESET+'|==D==E==S==S==O==F==/==D==E==S==S==O==F==')
        print('\nDistâncias: ')
        for i in paises:
            print('     {} --> {:.2f} km'.format(i[0], i[1]))
        print('Dicas: ')
        for i in dicasusadas:
            print('     - {}{}'.format(i, dicasusadas[i]))
        print()
    
def printa_status(paises,dicasusadas,tentativas):
    if paises != []:
        print("\nDistâncias:")
        for i in paises:
            if i[1] <= 1000:
                print(Fore.CYAN + '     {} --> {:.2f} km'.format(i[0], i[1]),end='')
            elif i[1] <= 2500:
                print(Fore.YELLOW + '     {} --> {:.2f} km'.format(i[0], i[1]),end='')
            elif i[1] <= 5000:
                print(Fore.RED + '     {} --> {:.2f} km'.format(i[0], i[1]),end='')
            elif i[1] <= 10000:
                print(Fore.LIGHTMAGENTA_EX + '     {} --> {:.2f} km'.format(i[0], i[1]),end='')
            else:
                print(Fore.LIGHTBLACK_EX + '     {} --> {:.2f} km'.format(i[0], i[1]),end='')
            print(Fore.RESET + '')
    if dicasusadas != {}:
        print("\nDicas:")
        for i in dicasusadas:
            print('     - {}{}'.format(i, dicasusadas[i]))
    print('\nVocê tem: {} tentativas sobrando!\n'.format(cor_tentativa(tentativas)))