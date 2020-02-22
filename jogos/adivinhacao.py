print("***********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("***********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):

    print("Tentativa: {} de {}". format(rodada, total_de_tentativas))
    chute = input("Digite o seu numero: ")
    numero = int(chute)

    print("Voce digitou ", chute)

    acertou = numero == numero_secreto
    maior = numero > numero_secreto
    menor = numero < numero_secreto

    if (acertou):
        print("Voce acertou!")
    else:

        if (maior):
            print("Voce errou! Seu chute foi maior que o numero secreto.")
        elif (menor):
            print("Voce errou! Seu chute foi menor que o numero secreto.")

    rodada = rodada + 1

print("Fim do jogo")