temperaturas = []
dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

for dia in dias:
    temp = float(input(f"Digite a temperatura de {dia}: "))
    temperaturas.append(temp)

soma = 0

for t in temperaturas:
    soma += t

media = soma / len(temperaturas)

print(f"Média da semana: {media:.2f}°C")