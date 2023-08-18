from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/estudiantes")
def estudiantes():
    data = [
        {"Matricula": "23007", "Nombre": "Euris", "Apellido_Paterno": "Liendo", "Apellido_Materno": "Cordero"},
        {"Matricula": "23008", "Nombre": "Fernando", "Apellido_Paterno": "Lozano", "Apellido_Materno": "Martínez"},
        {"Matricula": "23009", "Nombre": "Cecilia", "Apellido_Paterno": "Ramos", "Apellido_Materno": "León"},
        {"Matricula": "23010", "Nombre": "Alessandra", "Apellido_Paterno": "Bernardo", "Apellido_Materno": "Moreno"}
    ]
    return render_template("estudiantes.html", data = data)


if __name__ == '__main__':
    app.run(debug=True, port=8888)
