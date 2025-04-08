from flask import Flask, request, jsonify, send_from_directory, render_template
import mysql.connector
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Rota principal da página inicial
@app.route('/')
def home():
    return app.send_static_file('index.html')

# Rota de imagens já criada
@app.route('/img/<path:filename>')
def get_image(filename):
    return send_from_directory('../frontend/img', filename)

# Rota de cadastro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
