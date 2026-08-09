# Manual 100% completo - Vitrine Aurora

Este manual foi escrito para quem esta comecando. Siga na ordem, sem pular etapas.

## 1. Antes de abrir o VS Code

### Instalar o Python

1. Acesse https://www.python.org/downloads/.
2. Baixe o Python 3 para Windows.
3. Abra o instalador.
4. Na primeira tela, marque **Add python.exe to PATH**.
5. Clique em **Install Now**.
6. Aguarde terminar e clique em **Close**.

Para conferir, abra o Prompt de Comando e digite:

```bash
python --version
```

Se aparecer `Python 3.x.x`, esta correto.

### Instalar o Visual Studio Code

1. Acesse https://code.visualstudio.com/.
2. Baixe a versao para Windows.
3. Instale mantendo as opcoes padrao.
4. Abra o VS Code.
5. Clique em **Extensions** na lateral esquerda.
6. Procure por **Python**, da Microsoft, e clique em **Install**.

## 2. Abrir o projeto no VS Code

1. Descompacte o arquivo `Anna_Ecommerce_Flask.zip` em uma pasta facil de encontrar, por exemplo na Area de Trabalho.
2. Abra o VS Code.
3. Clique em **File > Open Folder**.
4. Selecione a pasta `Anna_Ecommerce_Flask`.
5. Clique em **Select Folder**.
6. Se aparecer a pergunta sobre confiar nos arquivos, confirme que confia no projeto.

No Explorer do VS Code devem aparecer `app.py`, `requirements.txt`, `templates` e `static`.

## 3. Abrir o terminal dentro do VS Code

1. No menu superior, clique em **Terminal > New Terminal**.
2. O terminal sera aberto na parte inferior.
3. Confira se o final do caminho exibido corresponde a pasta `Anna_Ecommerce_Flask`.

## 4. Criar o ambiente virtual

No terminal, digite:

```bash
python -m venv .venv
```

No Windows PowerShell, ative com:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativacao, abra um terminal **Command Prompt** no VS Code e use:

```cmd
.venv\Scripts\activate.bat
```

Quando funcionar, normalmente aparece `(.venv)` antes do caminho no terminal.

## 5. Instalar o Flask

Com o ambiente virtual ativado, execute:

```bash
python -m pip install -r requirements.txt
```

Espere a instalacao terminar. Para conferir:

```bash
python -m flask --version
```

## 6. Executar o sistema

No mesmo terminal:

```bash
python app.py
```

Deve aparecer um endereco parecido com:

```text
http://127.0.0.1:5000
```

Segure `Ctrl` e clique nesse endereco ou copie e cole no Chrome/Edge.

## 7. Testar o menu

Abra cada item do menu e confirme que carrega sem erro:

1. Inicio
2. Anuncios
3. Categorias
4. Perguntas
5. Favoritos
6. Compras
7. Usuarios
8. Relatorios > Minhas compras
9. Relatorios > Minhas vendas

Para parar o servidor, volte ao terminal e pressione `Ctrl + C`.

## 8. Entender os arquivos

```text
Anna_Ecommerce_Flask/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- static/
|   `-- style.css
`-- templates/
    |-- base.html
    |-- index.html
    |-- entidade.html
    `-- relatorio.html
```

- `app.py`: cria o aplicativo Flask e suas rotas.
- `templates/base.html`: possui o menu que se repete nas paginas.
- `templates/index.html`: pagina inicial.
- `templates/entidade.html`: modelo usado nas paginas das entidades.
- `templates/relatorio.html`: modelo dos relatorios.
- `static/style.css`: cores, espacamentos, cards, responsividade e layout.
- `requirements.txt`: registra a dependencia Flask.

## 9. Rotas implementadas

| URL | Funcao Python | Finalidade |
| --- | --- | --- |
| `/` | `inicio` | Pagina inicial |
| `/usuarios` | `usuarios` | Usuarios |
| `/categorias` | `categorias` | Categorias |
| `/anuncios` | `anuncios` | Anuncios |
| `/perguntas` | `perguntas` | Perguntas e respostas |
| `/compras` | `compras` | Compras |
| `/favoritos` | `favoritos` | Favoritos |
| `/relatorios/compras` | `relatorio_compras` | Relatorio de compras |
| `/relatorios/vendas` | `relatorio_vendas` | Relatorio de vendas |

## 10. MER utilizado

Entidades principais:

- **Usuario**: id_usuario, nome, email, senha.
- **Categoria**: id_categoria, nome, descricao.
- **Anuncio**: id_anuncio, titulo, descricao, preco, data_publicacao, id_usuario, id_categoria.
- **Pergunta**: id_pergunta, texto, data_pergunta, resposta, data_resposta, id_usuario, id_anuncio.
- **Compra**: id_compra, data_compra, quantidade, valor_total, id_comprador, id_anuncio.
- **Favorito**: id_favorito, data_adicao, id_usuario, id_anuncio.

Relacionamentos:

- Um usuario pode publicar varios anuncios; cada anuncio pertence a um usuario.
- Uma categoria pode classificar varios anuncios; cada anuncio possui uma categoria.
- Um usuario pode fazer varias perguntas; cada pergunta pertence a um usuario e a um anuncio.
- O proprietario do anuncio pode registrar a resposta da pergunta.
- Um usuario pode realizar varias compras; cada compra corresponde a um anuncio, sem carrinho.
- Usuario e anuncio possuem relacionamento muitos-para-muitos resolvido pela entidade Favorito.

## 11. Publicar no GitHub pelo site

### Criar a conta, se necessario

1. Acesse https://github.com/.
2. Clique em **Sign up**.
3. Crie a conta e confirme o e-mail.

### Criar o repositorio

1. Entre no GitHub.
2. No canto superior direito, clique no sinal **+**.
3. Clique em **New repository**.
4. Em **Repository name**, use por exemplo `vitrine-aurora-flask`.
5. Em visibilidade, marque **Public**. Isso e obrigatorio porque o enunciado pede endereco publico.
6. Nao precisa marcar a criacao automatica de README, pois o projeto ja possui um.
7. Clique em **Create repository**.

### Enviar pelo terminal do VS Code

Com o terminal aberto dentro da pasta do projeto, execute um comando por vez:

```bash
git init
git add .
git commit -m "Projeto inicial de e-commerce em Flask"
git branch -M main
git remote add origin URL_DO_REPOSITORIO
git push -u origin main
```

Troque `URL_DO_REPOSITORIO` pelo endereco que o GitHub mostrar, por exemplo:

```text
https://github.com/SEU-USUARIO/vitrine-aurora-flask.git
```

Se o comando `git` nao existir, instale o Git em https://git-scm.com/download/win e reabra o VS Code.

### Conferencia final no GitHub

1. Atualize a pagina do repositorio.
2. Confirme que aparecem `app.py`, `templates`, `static`, `README.md` e `requirements.txt`.
3. Confirme que o repositorio esta marcado como **Public**.
4. Copie o endereco da pagina do repositorio, sem `.git` no final.
5. Esse e o link que deve constar na entrega/PDF.

## 12. Antes de entregar

Checklist:

- [ ] Projeto abre e roda com `python app.py`.
- [ ] Todos os itens do menu funcionam.
- [ ] O MER esta no PDF.
- [ ] O diagrama de navegacao esta no PDF.
- [ ] O PDF possui justificativas.
- [ ] O repositorio GitHub esta publico.
- [ ] O link do GitHub foi colocado no PDF/atividade.
- [ ] O nome da aluna esta correto.
- [ ] A data de publicacao e compativel com o prazo da disciplina.

## Observacao sobre o link do GitHub

O arquivo PDF fornecido junto ao projeto traz um campo para preencher o endereco publico do GitHub depois que o repositorio for criado. O link nao pode ser inventado antes da publicacao.
