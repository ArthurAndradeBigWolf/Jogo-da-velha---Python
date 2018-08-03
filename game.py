import library
import os
#lista usada no jogo
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#dicionario usada no jogo
dicionario={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}


print(">>>>>>>> JOGO DA VELHA <<<<<<")
#VARIÁVEIS
k=0#CONDIÇÃO DO PRIMEIRO LOOP
j=0#CONDIÇÃO DO SEGUNDO LOOP
jogada=[]#JOGADA[linha,coluna]
destrave=0#JOGADAR 1 OU 2
jogo=0#VENCEDOR
jogadas=0
#--------------------------

while k != 1:
    #MENU
    op = 0
    print("1-JOGAR O JOGO")
    print("2-SAIR")
    op=int(input())
    #-----
    #OPÇÃO JOGAR
    if op == 1:
        while j!=1:

            #JOGADOR 1
            if destrave == 0:

                #VERIFICA SE DEU VELHA
                if jogadas == 9:
                    print('>> DEU VELHA!!! <<')
                    j = 1
                    break

                os.system('cls')
                library.imprime_tabuleiro(dicionario)
                #LENDO JOGADA
                jogada=library.jogador_1()
                os.system('cls')
                #MARCANDO JOGADA NA LISTA
                lista=library.marca_jogada1(lista,jogada,destrave)
                print(lista)

                #MARCANDO X OU 0 DE ACORDO COM JOGADAS NA LISTA
                dicionario=library.bola_ou_x(lista,dicionario)

                #IMPRIMINDO O TABULEIRO COM AS JOGADAS
                library.imprime_tabuleiro(dicionario)

                #VERIFICANDO SE HOUVE VITORIA
                jogo = library.verifica_vitoria(lista)

                if jogo == 1:
                    print("JOGADOR 1 VENCEU!!")
                    j = 1
                elif jogo == 10:
                    print("JOGADOR 2 VENCEU!!")
                    j = 1
                #--------------------------------
                jogadas+=1
                destrave = 1

            #JOGADOR 2
            elif destrave == 1:

                #VERICANDO SE DEU VELHA
                if jogadas == 9:
                    print(">> DEU VELHA!!! <<")
                    j = 1
                    break

                #LENDO JOGADA
                jogada=library.jogador_2()
                os.system('cls')
                #MARCANDO JOGADA NA LISTA
                lista=library.marca_jogada1(lista,jogada,destrave)
                print(lista)

                #MARCANDO X OU 0 DE ACORDO COM AS JOGADAS DA LISTA
                dicionario=library.bola_ou_x(lista,dicionario)

                #IMPRIMINDO TABULEIRO COM AS JOGADAS
                library.imprime_tabuleiro(dicionario)

                #VERIFICANDO SE HOUVE VITORIA
                jogo = library.verifica_vitoria(lista)

                if jogo == 1:
                    print("JOGADOR 1 VENCEU!!")
                    j = 1
                elif jogo == 10:
                    print("JOGADOR 2 VENCEU")
                    j = 1
                #------------------------------
                destrave = 0
                jogadas+=1

    #OPÇÃO SAIR
    elif op ==2 :
        k=0
        break
