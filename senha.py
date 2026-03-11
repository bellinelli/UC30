senha = input("Digite uma senha: ")

tem_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and tem_numero:
    print("Senha válida!")
else:
    print("Senha inválida!")