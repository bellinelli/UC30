def somadenumeros(numero1, numero2):
    soma = numero1 + numero2
    produto = numero1 * numero2
    
    print("Resultadosoma:", soma)
    print("Resultadomultiplicacao:", produto)

#---------------------------------------------------------------------------------------------------------------------------

def calcularsalario(ValorPHoras, HorasTrabalhadas):
    Saláriototal= ValorPHoras * HorasTrabalhadas
    return Saláriototal

total = calcularsalario(20, 40)
print("Salário total: ", total)
