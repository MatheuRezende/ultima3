from flask import Blueprint, request, jsonify
import mysql.connector
import os

routes = Blueprint('routes', __name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@routes.route('/pedidos', methods=['POST'])
def criar_pedido():
    data = request.get_json()
    descricao = data.get('descricao')
    usuario_id = data.get('usuario_id', 1)  # valor fixo para exemplo

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (usuario_id, descricao) VALUES (%s, %s)", (usuario_id, descricao))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Pedido criado com sucesso!'})