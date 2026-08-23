# Vitrine Aurora — Trilha 3

Projeto acadêmico de e-commerce desenvolvido em Flask por **Anna Julia Torres Martins de Deus**.

Nesta etapa, o sistema recebeu autenticação, controle de sessão, proteção das rotas internas e uma interface responsiva construída com Bootstrap 5.3.8.

## Acesso ao sistema

Páginas públicas:

- início;
- login;
- criação de conta.

Áreas protegidas por login:

- usuários;
- categorias;
- anúncios;
- perguntas e respostas;
- compras;
- favoritos;
- relatórios de compras e vendas;
- todas as operações de cadastro, edição e exclusão.

## Login para demonstração

- E-mail: `anna@email.com`
- Senha: `123456`

Também é possível criar uma conta na página de cadastro. As senhas são armazenadas em formato de hash, e não como texto puro.

## Tecnologias

- Python;
- Flask;
- Flask-SQLAlchemy;
- Flask-Login;
- SQLite;
- Bootstrap 5.3.8;
- HTML, CSS e Jinja.

## Como executar no Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

Depois, abra `http://127.0.0.1:5000` no navegador.

## Repositório público

https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git

## Sistema no PythonAnywhere

O endereço público será preenchido após a implantação:

`https://USUARIO.pythonanywhere.com`
