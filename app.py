from flask import Flask, render_template
from entidades.estudiantes import Estudiante
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/estudiantes")
def estudiantes():
    estudiantes = []
    with open("db/estudiantes.txt", "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            data = l.split("|")
            estudiantes.append(Estudiante(data[0], data[1], data[2], data[3]))

    return render_template("estudiantes.html", data=estudiantes)





if __name__ == '__main__':
    app.run(debug=True, port=8888)
