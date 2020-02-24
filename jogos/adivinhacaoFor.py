print("***********************************")
print("Bem vindo ao jogo de Adivinhacao!")
print("***********************************")

numero_secreto = 43
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa: {} de {}". format(rodada, total_de_tentativas))
    chute = input("Digite um numero entre 1 e 100: ")
    numero = int(chute)

    print("Voce digitou ", chute)

    if (numero < 1 or numero > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acertou = numero == numero_secreto
    maior = numero > numero_secreto
    menor = numero < numero_secreto

    if (acertou):
        print("Voce acertou!")
        break
    else:

        if (maior):
            print("Voce errou! Seu chute foi maior que o numero secreto.")
        elif (menor):
            print("Voce errou! Seu chute foi menor que o numero secreto.")

print("Fim do jogo")