# Plataforma de Autenticação de Usuários

Este projeto é uma aplicação web full-stack para cadastro e login de usuários, construída com Flask no backend e React no frontend. Possui autenticação JWT e um painel simples para o usuário.

## Sistema Online

Você pode acessar a versão online da aplicação em: [Seu Link do Sistema Online Aqui]

## Prints de Tela

### Processo de Cadastro
![Print do Cadastro](caminho/para/print_cadastro.png)

### Processo de Login
![Print do Login](caminho/para/print_login.png)

## Estrutura do Projeto

```
user-auth-platform
├── backend
│   ├── app.py
│   ├── models.py
│   ├── requirements.txt
│   ├── .env.example
│   └── README.md
├── frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── App.js
│   │   ├── components
│   │   │   ├── Register.js
│   │   │   ├── Login.js
│   │   │   └── Dashboard.js
│   │   └── index.js
│   ├── package.json
│   └── README.md
├── .github
│   └── workflows
│       └── ci.yml
└── README.md
```

## Configuração do Backend

1. Clone o repositório:
   ```
   git clone https://github.com/seuusuario/user-auth-platform.git
   cd user-auth-platform/backend
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:
   - Copie `.env.example` para `.env` e defina sua `SECRET_KEY`.

5. Execute a aplicação:
   ```
   python app.py
   ```

## Configuração do Frontend

1. Navegue até o diretório do frontend:
   ```
   cd ../frontend
   ```

2. Instale as dependências necessárias:
   ```
   npm install
   ```

3. Inicie a aplicação React:
   ```
   npm start
   ```

## CI/CD

Este projeto utiliza GitHub Actions para integração e entrega contínua. Você encontra a configuração do workflow em `.github/workflows/ci.yml`.

![Badge do GitHub Actions](https://github.com/seuusuario/user-auth-platform/workflows/CI/badge.svg)

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais