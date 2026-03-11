aluno = {}

# Solicitando os dados
aluno["nome"] = input("Digite o nome do aluno: ")
aluno["nota1"] = float(input("Digite a nota da Prova 1: "))
aluno["nota2"] = float(input("Digite a nota da Prova 2: "))

media = (aluno["nota1"] + aluno["nota2"]) / 2

# Adicionando a média ao dicionário
aluno["media"] = media

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

print("Situação:", situacao)