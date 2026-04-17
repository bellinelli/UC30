while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 5:
            print("Saindo da calculadora...")
            break

        if opcao >= 1 and opcao <= 4:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                print("Resultado:", n1 + n2)
            elif opcao == 2:
                print("Resultado:", n1 - n2)
            elif opcao == 3:
                print("Resultado:", n1 * n2)
            elif opcao == 4:
                if n2 == 0:
                    print("Erro: divisão por zero!")
                else:
                    print("Resultado:", n1 / n2)
        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: digite apenas números válidos.")