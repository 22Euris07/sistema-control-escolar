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
            print(estudiantes)

    return render_template("estudiantes.html", estudiantes=estudiantes)



from entidades.materias import Materia
@app.route("/materias")
def materias():
    materias = []
    with open("db/materias.txt", "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            data = l.split("|")
            materias.append(Materia(data[0], data[1], data[2]))
            print(materias)

    return render_template("materias.html", materias=materias)


from entidades.profesores import Profesores
@app.route("/profesores")
def profesores():
    profesores = []
    with open("db/profesores.txt", "r") as f:
        lines = f.read().splitlines()
        for l in lines:
            data = l.split("|")
            profesores.append(Profesores(data[0], data[1], data[2], data[3]))
            print(profesores)
            
    return render_template("profesores.html", profesores=profesores)



if __name__ == '__main__':
    app.run(debug=True, port=8888)
