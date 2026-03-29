from flask import Flask, jsonify
from conexion import conectar
import pandas as pd

app = Flask(__name__)

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    db = conectar()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        db.close()
        return jsonify(clientes)
    return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

@app.route('/api/cotizaciones', methods=['GET'])
def get_cotizaciones():
    db = conectar()
    if db:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM cotizaciones")
        cotizaciones = cursor.fetchall()
        db.close()
        return jsonify(cotizaciones)
    return jsonify({"error": "Error de conexión"}), 500

if __name__ == '__main__':
    print("🚀 Servidor API corriendo en http://127.0.0.1:5000")
    app.run(debug=True)