notas = [6.5, 8.0, 7.2, 5.9, 9.1, 7.0, 8.5]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print(f"Quantidade de notas acima de 7: {contador}")