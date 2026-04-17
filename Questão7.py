vendas = [10, 15, 22, 33, 40, 55, 60]

soma_pares = 0

for valor in vendas:
    if valor % 2 == 0:
        soma_pares += valor

print(f"Soma dos valores pares: {soma_pares}")