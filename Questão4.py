def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        return f"IMC: {imc:.2f} - Magro"
    elif imc <= 24.9:
        return f"IMC: {imc:.2f} - Normal"
    else:
        return f"IMC: {imc:.2f} - Acima do peso"


try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    resultado = calcular_imc(peso, altura)
    print(resultado)

except ValueError:
    print("Entrada inválida! Digite apenas números.")
except ZeroDivisionError:
    print("Altura não pode ser zero. Tu seria uma folha de papel?")