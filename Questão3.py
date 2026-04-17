total = 0.0

valor = float(input("Digite o valor do item (0 para encerrar): "))

while valor != 0:
    total += valor
    valor = float(input("Digite o valor do item (0 para encerrar): "))

print(f"Total da compra: R$ {total:.2f}")