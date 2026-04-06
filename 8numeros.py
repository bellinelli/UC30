numeros = []

print("Digite 8 números:")

for i in range(8):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

contagem = {}

for num in numeros:
    if num in contagem:
        contagem[num] += 1
    else:
        contagem[num] = 1

print("Números repetidos:")

repetido = False

for num, qtd in contagem.items():
    if qtd > 1:
        print(f"O número {num} apareceu {qtd} vezes")
        repetido = True

if not  repetido:
    print("Nenhum número foi repetido.")