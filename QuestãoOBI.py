# Pão = 1 ponto
# Doce =  2 pontos
# Bolo = 3 pontos
# Se soma => 150 Colaborador recebe 1 bolo, => 120 Doce, =>100 pão, 100 > pontos = nada
# Pão + Doce + Bolo = 150

# Programa que: Dados os números dos pães, doces e bolos vendidos, determinar o prêmio merecido]

P = int(input())
D = int(input())
B = int(input())

pontos = P * 1 + D * 2 + B * 3

if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")
