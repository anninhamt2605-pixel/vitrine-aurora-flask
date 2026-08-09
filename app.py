from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    destaques = [
        {"titulo": "Anuncios ativos", "valor": "24", "cor": "violeta"},
        {"titulo": "Categorias", "valor": "6", "cor": "menta"},
        {"titulo": "Perguntas abertas", "valor": "8", "cor": "laranja"},
    ]
    return render_template("index.html", destaques=destaques)


@app.route("/usuarios")
def usuarios():
    itens = [
        {"titulo": "Anna", "descricao": "Compradora e anunciante", "detalhe": "anna@email.com"},
        {"titulo": "Marina Costa", "descricao": "Compradora", "detalhe": "marina@email.com"},
        {"titulo": "Lucas Lima", "descricao": "Anunciante", "detalhe": "lucas@email.com"},
    ]
    return render_template("entidade.html", titulo="Usuarios", subtitulo="Pessoas cadastradas na plataforma", itens=itens)


@app.route("/categorias")
def categorias():
    itens = [
        {"titulo": "Eletronicos", "descricao": "Celulares, notebooks e acessorios", "detalhe": "9 anuncios"},
        {"titulo": "Casa e decoracao", "descricao": "Itens para todos os ambientes", "detalhe": "7 anuncios"},
        {"titulo": "Livros", "descricao": "Livros novos e usados", "detalhe": "8 anuncios"},
    ]
    return render_template("entidade.html", titulo="Categorias", subtitulo="Organizacao dos anuncios por assunto", itens=itens)


@app.route("/anuncios")
def anuncios():
    itens = [
        {"titulo": "Fone Bluetooth", "descricao": "Eletronicos - anunciado por Anna", "detalhe": "R$ 129,90"},
        {"titulo": "Luminaria de mesa", "descricao": "Casa e decoracao - anunciado por Lucas", "detalhe": "R$ 79,00"},
        {"titulo": "Livro de Python", "descricao": "Livros - anunciado por Marina", "detalhe": "R$ 65,00"},
    ]
    return render_template("entidade.html", titulo="Anuncios", subtitulo="Produtos disponiveis para compra", itens=itens)


@app.route("/perguntas")
def perguntas():
    itens = [
        {"titulo": "O produto possui garantia?", "descricao": "Pergunta no anuncio Fone Bluetooth", "detalhe": "Respondida"},
        {"titulo": "Voce envia para outro estado?", "descricao": "Pergunta no anuncio Livro de Python", "detalhe": "Aguardando resposta"},
        {"titulo": "Qual a altura da luminaria?", "descricao": "Pergunta no anuncio Luminaria de mesa", "detalhe": "Respondida"},
    ]
    return render_template("entidade.html", titulo="Perguntas", subtitulo="Duvidas feitas pelos usuarios nos anuncios", itens=itens)


@app.route("/compras")
def compras():
    itens = [
        {"titulo": "Compra #1042", "descricao": "Fone Bluetooth - 1 unidade", "detalhe": "R$ 129,90"},
        {"titulo": "Compra #1043", "descricao": "Livro de Python - 1 unidade", "detalhe": "R$ 65,00"},
        {"titulo": "Compra #1044", "descricao": "Luminaria de mesa - 1 unidade", "detalhe": "R$ 79,00"},
    ]
    return render_template("entidade.html", titulo="Compras", subtitulo="Compras realizadas diretamente em um anuncio", itens=itens)


@app.route("/favoritos")
def favoritos():
    itens = [
        {"titulo": "Fone Bluetooth", "descricao": "Salvo por Anna", "detalhe": "Eletronicos"},
        {"titulo": "Livro de Python", "descricao": "Salvo por Anna", "detalhe": "Livros"},
    ]
    return render_template("entidade.html", titulo="Favoritos", subtitulo="Anuncios salvos para consultar depois", itens=itens)


@app.route("/relatorios/compras")
def relatorio_compras():
    dados = [
        {"item": "Fone Bluetooth", "pessoa": "Anna", "data": "02/08/2026", "valor": "R$ 129,90"},
        {"item": "Livro de Python", "pessoa": "Anna", "data": "04/08/2026", "valor": "R$ 65,00"},
    ]
    return render_template("relatorio.html", titulo="Relatorio de compras", pessoa_label="Comprador", dados=dados, total="R$ 194,90")


@app.route("/relatorios/vendas")
def relatorio_vendas():
    dados = [
        {"item": "Fone Bluetooth", "pessoa": "Marina Costa", "data": "03/08/2026", "valor": "R$ 129,90"},
        {"item": "Capa para celular", "pessoa": "Lucas Lima", "data": "05/08/2026", "valor": "R$ 45,00"},
    ]
    return render_template("relatorio.html", titulo="Relatorio de vendas", pessoa_label="Comprador", dados=dados, total="R$ 174,90")


if __name__ == "__main__":
    app.run(debug=True)
