print("***********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("***********************************")

numero_secreto = 43

chute = input("Digite o seu numero: ")
numero = int(chute)

print("Voce digitou ", chute)

if (numero_secreto == numero):
    print("Voce acertou!")
else:
    print("Voce errou")

print("Fim do jogo")