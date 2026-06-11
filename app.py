from flask import Flask, render_template, request, redirect, session
from database import (
    crear_tabla,
    guardar_prospecto,
    obtener_prospectos,
    eliminar_prospecto
)

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-en-produccion"

crear_tabla()


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    correo = request.form.get("correo", "")
    mensaje = request.form["mensaje"]

    guardar_prospecto(nombre, telefono, correo, mensaje)

    return redirect("/#contacto")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        if usuario == "admin" and password == "1234":
            session["login"] = True
            return redirect("/panel")

    return render_template("login.html")


@app.route("/panel")
def panel():
    if not session.get("login"):
        return redirect("/login")

    prospectos = obtener_prospectos()
    total = len(prospectos)

    return render_template(
        "panel.html",
        prospectos=prospectos,
        total=total
    )


@app.route("/eliminar/<int:id>")
def eliminar(id):
    if not session.get("login"):
        return redirect("/login")

    eliminar_prospecto(id)
    return redirect("/panel")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)