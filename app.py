from flask import Flask, render_template

app = Flask(__name__)

# Lista de produtos
produtos = [
    {
        "nome": "X-Burguer",
        "descricao": "Hambúrguer artesanal com queijo",
        "preco": "R$ 30",
        "imagem": "burger.jpg"
    },
    {
        "nome": "Pizza",
        "descricao": "Pizza grande de calabresa",
        "preco": "R$ 45",
        "imagem": "pizza.jpg"
    },
    {
        "nome": "Batata Frita",
        "descricao": "Batata crocante com cheddar",
        "preco": "R$ 20",
        "imagem": "batata.jpg"
    },
    {
        "nome": "Milkshake",
        "descricao": "Milkshake de chocolate",
        "preco": "R$ 18",
        "imagem": "milkshake.jpg"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cardapio")
def cardapio():
    return render_template(
        "cardapio.html",
        produtos=produtos
    )


@app.route("/lanche/<nome>")
def lanche(nome):

    mensagem = ""

    if nome.lower() == "pizza":
        mensagem = "Você escolheu uma deliciosa pizza!"

    elif nome.lower() == "hamburguer":
        mensagem = "Hambúrguer saindo quentinho!"

    elif nome.lower() == "batata":
        mensagem = "Batata frita super crocante!"

    elif nome.lower() == "milkshake":
        mensagem = "Milkshake geladinho chegando!"

    else:
        mensagem = "Lanche não encontrado."

    return render_template(
        "lanche.html",
        nome=nome,
        mensagem=mensagem
    )


@app.route("/pedidos")
def pedidos():

    lista_pedidos = [
        {
            "cliente": "Ana",
            "pedido": "Pizza",
            "valor": "R$ 45"
        },
        {
            "cliente": "Pedro",
            "pedido": "X-Burguer",
            "valor": "R$ 30"
        },
        {
            "cliente": "Carlos",
            "pedido": "Batata Frita",
            "valor": "R$ 20"
        }
    ]

    return render_template(
        "pedidos.html",
        pedidos=lista_pedidos
    )


@app.route("/cliente/<nome>/<cidade>")
def cliente(nome, cidade):

    if cidade.lower() == "natal":
        status = "Entrega disponível!"
    else:
        status = "Entrega indisponível."

    return render_template(
        "cliente.html",
        nome=nome,
        cidade=cidade,
        status=status
    )


@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
