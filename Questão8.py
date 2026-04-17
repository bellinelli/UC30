valor = float(input("Digite o valor da compra: R$ "))

if valor > 500:
    desconto = 0.20
elif valor >= 200:
    desconto = 0.10
else:
    desconto = 0.0

preco_final = valor * (1 - desconto)

print(f"Preço final: R$ {preco_final:.2f}")