def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero não é permitida!"
    return a / b

while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("Encerrando a calculadora...")
        break

    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Tente novamente.")
        continue

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.")
        continue

    if opcao == "1":
        print("Resultado:", soma(num1, num2))
    elif opcao == "2":
        print("Resultado:", subtracao(num1, num2))
    elif opcao == "3":
        print("Resultado:", multiplicacao(num1, num2))
    elif opcao == "4":
        print("Resultado:", divisao(num1, num2))
