import random

adivinhar_numero = random.radiant(1, 100)
tentativas = 0

print("Tente adivinhar o número de 1 a 100: ")
while True:
    palpite = int(input("Digite o seu palpite "))
    tentativa += 1

    if palpite < adivinhar_numero:
        print("Maior!")
    elif palpite > adivinhar_numero:
        print("Menor!")
    else:
        print("Parabéns! Você acertou!")

print(f"Você precisou de {tentativas} para tentar acertar o número.")

