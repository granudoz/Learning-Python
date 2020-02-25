import random


def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de Adivinhacao!")
    print("***********************************")

    numero_secreto = random.randrange(1, 101)  # Gera numero aleatorio entre 1 e 100
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("Facil (1) Medio (2) Dificil (3)")

    nivel = int(input("Escolha o nivel de dificuldade: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("Tentativa: {} de {}".format(rodada,
                                           total_de_tentativas))  # utilizando interpolacao de string para melhor legibilidade do codigo
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
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:

            if (maior):
                print("Voce errou! Seu chute foi maior que o numero secreto.")
            elif (menor):
                print("Voce errou! Seu chute foi menor que o numero secreto.")

            pontos_perdidos = abs(numero_secreto - numero)  # Devolve o numero absoluto, ou seja, independente do sinal
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")


if (__name__ == "__main__"):  # Caso o arquivo seja executado diretamente chama a funcao jogar()
    jogar()
