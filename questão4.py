@app.route('/operacao/<tipo>/<float:op1>/<float:op2>')
def operacao(tipo, op1, op2):
    if tipo == "sum":
        resultado = op1 + op2
    elif tipo == "sub":
        resultado = op1 - op2
    elif tipo == "mult":
        resultado = op1 * op2
    elif tipo == "div":
        if op2 == 0:
            return "Erro: divisão por zero"
        resultado = op1 / op2
    else:
        return "Tipo de operação inválido"

    return f"Resultado: {resultado}"
