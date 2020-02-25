import forca
import adivinhacao

print("***********************************")
print("************Bem vindo**************")
print("***********************************")

print("Forca (1) Adivinhacao(2)")
jogo = int(input("Escolha seu jogo: "))

if (jogo == 1):
    forca.jogar()
elif (jogo == 2):
    adivinhacao.jogar()
