
def jogador_1():
    print(">>> JOGADOR 1")
    linha = int(input("DIGITE A LINHA:\t"))
    coluna = int(input("DIGITE A COLUNA:\t"))
    jogada = [linha, coluna]
    return jogada
#----------------------------------------------
def jogador_2():
    print(">>> JOGADOR 2")
    linha = int(input("DIGITE A LINHA:\t"))
    coluna = int(input("DIGITE A COLUNA:\t"))
    jogada = [linha, coluna]
    return jogada
#----------------------------------------------
#MARCA X OU O DE ACORDO COM A JOGADA
def bola_ou_x(lista,dicionario):
    #posição 1
    if lista[0] == 0:
        dicionario[1]='X'
    elif lista[0]== 10:
        dicionario[1]='O'
    else:
        dicionario[1]=' '

    #posição 2
    if lista[1] == 0:
        dicionario[2]='X'
    elif lista[1]== 10:
        dicionario[2]='O'
    else:
        dicionario[2]=' '

    #posição 3
    if lista[2] == 0:
        dicionario[3]='X'
    elif lista[2]== 10:
        dicionario[3]='O'
    else:
        dicionario[3]=' '

    #posição 4
    if lista[3] == 0:
        dicionario[4]='X'
    elif lista[3]== 10:
        dicionario[4]='O'
    else:
        dicionario[4]=' '

    #posição 5
    if lista[4] == 0:
        dicionario[5]='X'
    elif lista[4]== 10:
        dicionario[5]='O'
    else:
        dicionario[5]=' '

    #posição 6
    if lista[5] == 0:
        dicionario[6]='X'
    elif lista[5]== 10:
        dicionario[6]='O'
    else:
        dicionario[6]=' '

    #posição 7
    if lista[6] == 0:
        dicionario[7]='X'
    elif lista[6]== 10:
        dicionario[7]='O'
    else:
        dicionario[7]=' '

    #posição 8
    if lista[7] == 0:
        dicionario[8]='X'
    elif lista[7]== 10:
        dicionario[8]='O'
    else:
        dicionario[8]=' '

    #posição 9
    if lista[8] == 0:
        dicionario[9]='X'
    elif lista[8]== 10:
        dicionario[9]='O'
    else:
        dicionario[9]=' '

    return dicionario
    #-----------------------------------------------


def imprime_tabuleiro(dicionario):
    print('|------|------|------|')
    print('|  {}   |  {}   |  {}   |'.format(dicionario[1],dicionario[2],dicionario[3]))
    print('|------|------|------|')
    print('|  {}   |  {}   |  {}   |'.format(dicionario[4],dicionario[5],dicionario[6]))
    print('|------|------|------|')
    print('|  {}   |  {}   |  {}   |'.format(dicionario[7],dicionario[8],dicionario[9]))
    print('|------|------|------|')

#MARCANDO A JOGADA DOS JOGADORES
def marca_jogada1(lista,jogada,destrave):
    #linha 1 e coluna 1
    if ((jogada[0] == 1) and (jogada[1] == 1)):

            if destrave == 0:
                lista[0]= 0
                return lista
            elif destrave == 1:
                lista[0]= 10
                return lista

    #-------------------
    #linha 1 e coluna 2
    elif ((jogada[0] == 1) and (jogada[1] == 2)):

        if destrave == 0:
            lista[1]=0
            return lista
        elif destrave == 1:
            lista[1]=10
            return lista

    #------------------
    #linha 1 e coluna 3
    elif ((jogada[0] ==1) and (jogada[1] == 3)):

        if destrave == 0:
            lista[2]=0
            return lista
        elif destrave == 1:
            lista[2]=10
            return lista

    #-----------------
    #linha 2 e coluna 1
    elif ((jogada[0] ==2) and (jogada[1] == 1)):

        if destrave == 0:
            lista[3]=0
            return lista
        elif destrave == 1:
            lista[3]=10
            return lista

    #-----------------
    #linha 2 e coluna 2
    elif ((jogada[0] ==2) and (jogada[1] == 2)):

        if destrave == 0:
            lista[4]=0
            return lista
        elif destrave == 1:
            lista[4]=10
            return lista

    #-----------------
    #linha 2 e coluna 3
    elif ((jogada[0] ==2) and (jogada[1] == 3)):

        if destrave == 0:
            lista[5]=0
            return lista
        elif destrave == 1:
            lista[5]=10
            return lista

    #-----------------
    #linha 3 e coluna 1
    elif ((jogada[0] ==3) and (jogada[1] == 1)):

        if destrave == 0:
            lista[6]=0
            return lista
        elif destrave == 1:
            lista[6]=10
            return lista

    #-----------------
    #linha 3 e coluna 2
    elif ((jogada[0] == 3) and (jogada[1] == 2)):

        if destrave == 0:
            lista[7]=0
            return lista
        elif destrave == 1:
            lista[7]=10
            return lista

    #-----------------
    #linha 3 e coluna 3
    elif ((jogada[0] == 3) and (jogada[1] == 3)):

        if destrave == 0:
            lista[8]=0
            return lista
        elif destrave == 1:
            lista[8]=10
            return lista

    #-----------------
    #-----------------------------------------------------

#FUNÇÃO QUE VERIFICA VITORIA
def verifica_vitoria(lista):
    #primeira linha
    if ((lista[0] == 0) and (lista[1] == 0) and (lista[2] == 0)):
        return 1

    elif ((lista[0] == 10) and (lista[1] == 10) and (lista[2] == 10)):
        return 10

    #primeira coluna
    elif ((lista[0] == 0) and (lista[3] == 0) and (lista[6] == 0)):
        return 1
    elif ((lista[0] == 10) and (lista[3] == 10) and (lista[6] == 10)):
        return 10

    #segunda linha
    elif ((lista[3] == 0) and (lista[4] == 0) and (lista[5] == 0)):
        return 1
    elif ((lista[3] == 10) and (lista[4] == 10) and (lista[5] == 10)):
        return 10

    #terceira linha
    elif ((lista[6] == 0) and (lista[7] == 0) and (lista[8] == 0)):
        return 1
    elif ((lista[6] == 10) and (lista[7] == 10) and (lista[8] == 10)):
        return 10

    #segunda coluna
    elif ((lista[1] == 0) and (lista[4] == 0) and (lista[7] == 0)):
        return 1
    elif ((lista[1] == 10) and (lista[4] == 10) and (lista[7] == 10)):
        return 10

    #terceira COLUNA
    elif ((lista[2] == 0) and (lista[5] == 0) and (lista[8] == 0)):
        return 1
    elif ((lista[2] == 10) and (lista[5] == 10) and (lista[8] == 10)):
        return 10

    #DIAGONAL 1
    elif ((lista[0] == 0) and (lista[4]== 0) and (lista[8] == 0)):
        return 1
    elif ((lista[0] == 10) and (lista[4] == 10) and (lista[8] == 10)):
        return 10
    #DIAGONAL 2
    elif ((lista[2] == 0) and (lista[4] == 0) and (lista[6] == 0)):
        return 1
    elif ((lista[2] == 10) and (lista[4] == 10) and (lista[6] == 10)):
        return 10
    else:
        return 0
#----------------------------------------------------------
