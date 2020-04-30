#Autor: Pedro França
#Pedra, Papel, Tesoura
import random
print ("Bem Vindo!")
print ("Este é um jogo de Pedra, Papel, e Tesoura.")
print ("As Regras deste jogo são:")
print ("O jogador tem que escolher entre: Tesoura, o Papel, e Pedra.\nPara ganhar o jogo é muito simples, a tesoura ganha do papel, a pedra ganha da tesoura e o papel ganha da pedra.\nCaso aconteça de ambos jogadores escolherem um mesmo símbolo ocorrerá um empate.")
P1 = input ("Escolha entre Pedra, Papel e Tesoura:")
PPT = ['pedra', 'papel', 'tesoura']
Maquina = (random.choice(PPT))
print ("3...")
print ("2...")
print ("1...")
print ("JÁ!")
if Maquina == 'pedra' and P1 == 'tesoura':
    print ("A maquina ganhou!\nA máquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'papel' and P1 == 'pedra':
    print ("A maquina ganhou!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'tesoura' and P1 == 'papel':
    print ("A maquina ganhou!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'pedra' and P1 == 'papel':
    print ("Você ganhou!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'papel' and P1 == 'tesoura':
    print ("Você ganhou!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)    
if Maquina == 'tesoura' and P1 == 'pedra':
    print ("Você ganhou!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'pedra' and P1 == 'pedra':
    print ("Ocorreu um empate!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'tesoura' and P1 == 'tesoura':
    print ("Ocorreu um empate!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
if Maquina == 'papel' and P1 == 'papel':
    print ("Ocorreu um empate!\nA maquina escolheu:",Maquina,"O jogador escolheu:",P1)
else:
    print ("Palavra invalida!\nTente novamente!")
