from flask import Flask, render_template, request

app = Flask(__name__)

# Mostrar la calculadora
@app.route("/")
def inicio():
    return render_template("calculadora.html", resultado="")

# Procesar cálculo
@app.route("/calcular", methods=["POST"])
def calcular():
    num1 = float(request.form.get("num1"))
    num2 = float(request.form.get("num2"))
    operacion = request.form.get("operacion")

    if operacion == "sumar":
        resultado = num1 + num2
    elif operacion == "restar":
        resultado = num1 - num2
    elif operacion == "multiplicar":
        resultado = num1 * num2
    elif operacion == "dividir":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: división por cero"

    return render_template("calculadora.html", resultado=f"Resultado: {resultado}")

if __name__ == "__main__":
    app.run(debug=True)