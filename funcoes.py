print("Python é fácil")
print("Python é fácil")
print("Python é fácil")

def exibirmensagem():
    print("Olá, mundo!")

exibirmensagem()

def saudar(nome):
    print(f"Olá, {nome}!")

saudar("Ana")
saudar("Bruno")

def exibirmensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirmensagem("Ana", "Bom dia!")

exibirmensagem(nome ="Bruno", mensagem = "Boa noite!")

def calcularmedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularmedia(8.0, 9.0)
print(f"Média: {resultado}")