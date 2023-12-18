from flask import Flask, url_for, render_template

# inicializacao
app = Flask(__name__)


# rotas
@app.route("/")
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Joao", "membro_ativo": False},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template("index.html", titulo=titulo, usuarios=usuarios)


@app.route("/sobre")
def pagina_sobre():
    return """
        <b>ProgramadorPython</b>: assista os videos no 
        <a href="https://youtube.com/@programadorpython">Canal no Youtube</a>
    """


# execucao
app.run(debug=True)
