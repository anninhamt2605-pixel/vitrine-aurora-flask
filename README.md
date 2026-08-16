# Vitrine Aurora — Trilha 2

Continuação do projeto acadêmico de e-commerce desenvolvido em Flask por **Anna Julia Torres Martins de Deus**.

Nesta etapa, os dados deixaram de ser apenas exemplos escritos nas páginas e passaram a ser armazenados em um banco SQLite. O sistema possui CRUD completo para todas as entidades previstas no MER.

## Funcionalidades

- CRUD de usuários;
- CRUD de categorias;
- CRUD de anúncios;
- CRUD de perguntas e respostas;
- CRUD de compras diretas, sem carrinho;
- CRUD de favoritos;
- relatórios de compras e vendas atualizados a partir do banco de dados;
- confirmação antes de cada exclusão.

## Tecnologias

- Python;
- Flask;
- Flask-SQLAlchemy;
- SQLite;
- HTML, CSS e Jinja.

## Como executar

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Depois, abra `http://127.0.0.1:5000` no navegador.

O arquivo `vitrine_aurora.db` é criado automaticamente na primeira execução.

## Repositório

https://github.com/anninhamt2605-pixel/vitrine-aurora-flask.git
