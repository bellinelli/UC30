from flask import Flask, render_template

app = Flask(__name__)

@app.route('/arearestrita/<int:id>')
def area_restrita(id):
    if id == 1:
        imagem = "cadeado_fechado.png"
    elif id == 2:
        imagem = "cadeado_aberto.png"
    else:
        return "ID inválido"

    return f'<img src="/static/{imagem}">'
