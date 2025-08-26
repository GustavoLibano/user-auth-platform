from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import jwt
import datetime
import os
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configurações
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "segredo_dev")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Modelo de Usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)

# Criar banco de dados
with app.app_context():
    db.create_all()

# Rota de Registro
@app.route('/registrar', methods=['POST'])
def registrar():
    dados = request.json
    senha_hash = bcrypt.generate_password_hash(dados['senha']).decode('utf-8')
    novo_usuario = Usuario(nome_usuario=dados['nome_usuario'], senha=senha_hash)
    try:
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201
    except:
        return jsonify({"erro": "Usuário já existe!"}), 400

# Rota de Login
@app.route('/login', methods=['POST'])
def login():
    dados = request.json
    usuario = Usuario.query.filter_by(nome_usuario=dados['nome_usuario']).first()
    if usuario and bcrypt.check_password_hash(usuario.senha, dados['senha']):
        token = jwt.encode({
            'usuario_id': usuario.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({"token": token})
    return jsonify({"erro": "Credenciais inválidas"}), 401

# Rota Protegida (Painel)
@app.route('/painel', methods=['GET'])
def painel():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"erro": "Token ausente"}), 401
    try:
        decodificado = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        usuario = Usuario.query.get(decodificado['usuario_id'])
        return jsonify({"mensagem": f"Bem-vindo {usuario.nome_usuario}!"})
    except:
        return jsonify({"erro": "Token inválido"}), 401

if __name__ == '__main__':
    app.run(debug=True)