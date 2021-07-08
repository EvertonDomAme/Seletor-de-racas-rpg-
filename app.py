from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def index():
    nome = None
    sobrenome = None
    criatura = None
    imagem = None

    if request.method == 'POST': 
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        criatura = request.form['criatura']

        if criatura == "elfo":
            imagem = "https://i.pinimg.com/originals/e5/af/06/e5af06834f26fe465ae65ed9fc48064f.png" # imagem de elfo
        elif criatura == "orc":
            imagem = "https://i.pinimg.com/originals/c8/f6/7a/c8f67a7c1364d73d7b8e6d7b0552c988.png" # imagem do orc
        elif criatura == "hobbit":
            imagem = "https://i.pinimg.com/originals/a9/6b/10/a96b10c5c6c8038c3a38f89cae3c1c93.png" # imagem do hobbit
        elif criatura == "humano":
            imagem = "https://i.pinimg.com/originals/1f/37/15/1f371558235abb030d50d18613979395.png" # imagem do humano
        elif criatura == "anão":
            imagem = "https://i.pinimg.com/originals/ea/e9/8c/eae98c0a01f2beb627079c205c4761f8.png" # imagem do anao
        else:
            imagem = None

    return render_template("index.html", nome=nome, sobrenome=sobrenome, criatura=criatura, imagem=imagem)

if (__name__ == "__main__"):
    app.run(debug=True) 