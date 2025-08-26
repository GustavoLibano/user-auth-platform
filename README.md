# 🔐 User Auth Platform

Aplicação **Fullstack** simples para autenticação de usuários utilizando **Flask (Python)** no backend e **React** no frontend.  
Inclui registro, login com senha criptografada e autenticação JWT, além de um **painel protegido** que só pode ser acessado com token válido.

---

## 🚀 Tecnologias

### Backend
- [Flask](https://flask.palletsprojects.com/) — microframework Python
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) — ORM para banco de dados
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) — hash seguro de senhas
- [PyJWT](https://pyjwt.readthedocs.io/) — geração/validação de tokens JWT
- [Flask-CORS](https://flask-cors.readthedocs.io/) — integração entre frontend e backend
- [SQLite](https://www.sqlite.org/) — banco de dados local simples
- [python-dotenv](https://pypi.org/project/python-dotenv/) — gerenciamento de variáveis de ambiente

### Frontend
- [React](https://reactjs.org/) — interface do usuário
- [React Router DOM](https://reactrouter.com/) — rotas SPA
- [Axios](https://axios-http.com/) — chamadas HTTP
- HTML + CSS básicos

---

## ⚙️ Funcionalidades

- 📌 **Registro de Usuário** com senha criptografada (`bcrypt`)  
- 🔑 **Login** e emissão de **JWT Token**  
- 🛡 **Rota protegida** que só pode ser acessada com token válido  
- 🎨 **Frontend React** com páginas de Registro, Login e Dashboard  
- ✅ Armazenamento de token no `localStorage`  

---

## 📂 Estrutura do Projeto

/backend
│ app.py
│ models.py
│ requirements.txt
│ .env
│
/frontend
│ public/
│ src/
│ components/
│ Register.js
│ Login.js
│ Dashboard.js
│ App.js
│ index.js
│ package.json
│


---


---

## 🛠 Como rodar o projeto

### 1. Clonar repositório
```bash
git clone https://github.com/seu-usuario/user-auth-platform.git
cd user-auth-platform

2. Rodar o backend (Flask)
cd backend
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
flask run

3. Rodar o frontend (React)

cd frontend
npm install
npm start

🔑 Exemplos de Rotas (Backend)
Registro

POST /registrar
Content-Type: application/json

{
  "nome_usuario": "gustavo",
  "senha": "123456"
}

Login

POST /login
Content-Type: application/json

{
  "nome_usuario": "gustavo",
  "senha": "123456"
}
Resposta:
{ "token": "eyJhbGciOiJIUzI1NiIsIn..." }
Painel (Protegido)
GET /painel
Authorization: <token>
Resposta:
{ "mensagem": "Bem-vindo gustavo!" }

🎯 Próximos Passos / Melhorias

✅ Deploy backend no Render/Heroku

✅ Deploy frontend no Vercel/Netlify

🔄 Refresh token para sessões mais longas

👤 Recuperação de senha via email

📊 Integração com banco SQL (PostgreSQL/MySQL)

📝 Licença

Este projeto é de uso livre para fins educacionais e de portfólio.

---
