import jogar_aleatorio  #importando os jogos
import jogar_advinhacao

print("*********************************")
print("*******Escolha o seu jogo!*******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if (jogo == 1):
    print("Jogando forca")
    jogar_aleatorio.jogar()  #aplicando o codigo = nome .jogar()
elif (jogo == 2):
    print("Jogando adivinhação")
    jogar_advinhacao.jogar()