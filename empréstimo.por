programa
{
	funcao inicio()
	{
		// Declaração de variáveis
		real valor_casa, salario, prestacao, limite_salario
		inteiro anos, meses

		// Entrada de dados
		escreva("Qual o valor da casa? R$ ")
		leia(valor_casa)

		escreva("Qual o salário do comprador? R$ ")
		leia(salario)

		escreva("Em quantos anos pretende pagar? ")
		leia(anos)

		// Cálculos
		meses = anos * 12
		prestacao = valor_casa / meses
		limite_salario = salario * 0.30

		// Saída de resultados e Verificação
		escreva("\n--- Resultado da Análise ---\n")
		escreva("Valor da prestação: R$ ", prestacao, "\n")
		
		se (prestacao <= limite_salario) 
		{
			escreva("Empréstimo APROVADO! Devolva depois hein.")
		}
		senao 
		{
			escreva("Empréstimo NEGADO. A parcela excede 30% do seu salário (R$ ", limite_salario, ").")
		}
	}
}