total = 0
transacoes = 0

while True:
    deposito = float(input("Digite o valor do depósito (0 para sair): "))

    if deposito == 0:
        break

    total += deposito
    transacoes += 1

print("Total depositado:", total)
print("Quantidade de transações:", transacoes)