import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao jogo de Adivinhar o Número!")
    print("Tente adivinhar o número entre 1 e 100.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

    else:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    adivinhar_numero()