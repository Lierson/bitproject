from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

# Desenvolvido por: Lierson de Paula Rodrigues
# Data: 14 de março de 2023

@app.route("/")
def index():
    return render_template("/template/index.html")

@app.route("/update")
def update():
    # Obtém a porcentagem de uso de CPU
    cpu_usage = psutil.cpu_percent()

    # Converte a porcentagem em bits
    bits = round(cpu_usage * 64 / 100)

    # Renderiza o template HTML com os resultados
    return jsonify({
        "cpu_usage": cpu_usage,
        "bits": bits
    })

if __name__ == "__main__":
    app.run(debug=True)
