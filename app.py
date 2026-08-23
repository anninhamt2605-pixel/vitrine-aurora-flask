import os
from datetime import date, datetime
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "vitrine-aurora-chave-academica")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", f"sqlite:///{BASE_DIR / 'vitrine_aurora.db'}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Faça login para acessar esta página."
login_manager.login_message_category = "aviso"


@event.listens_for(Engine, "connect")
def ativar_chaves_estrangeiras(conexao, _):
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Usuario(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)

    anuncios = db.relationship("Anuncio", back_populates="usuario", cascade="all, delete-orphan")
    perguntas = db.relationship("Pergunta", back_populates="usuario", cascade="all, delete-orphan")
    compras = db.relationship("Compra", back_populates="comprador", cascade="all, delete-orphan")
    favoritos = db.relationship("Favorito", back_populates="usuario", cascade="all, delete-orphan")

    def definir_senha(self, senha):
        self.senha = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)


@login_manager.user_loader
def carregar_usuario(usuario_id):
    return db.session.get(Usuario, int(usuario_id))


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    descricao = db.Column(db.String(250), nullable=False)

    anuncios = db.relationship("Anuncio", back_populates="categoria", cascade="all, delete-orphan")


class Anuncio(db.Model):
    __tablename__ = "anuncios"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data_publicacao = db.Column(db.Date, nullable=False, default=date.today)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id", ondelete="CASCADE"), nullable=False)

    usuario = db.relationship("Usuario", back_populates="anuncios")
    categoria = db.relationship("Categoria", back_populates="anuncios")
    perguntas = db.relationship("Pergunta", back_populates="anuncio", cascade="all, delete-orphan")
    compras = db.relationship("Compra", back_populates="anuncio", cascade="all, delete-orphan")
    favoritos = db.relationship("Favorito", back_populates="anuncio", cascade="all, delete-orphan")


class Pergunta(db.Model):
    __tablename__ = "perguntas"

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    data_pergunta = db.Column(db.Date, nullable=False, default=date.today)
    resposta = db.Column(db.Text)
    data_resposta = db.Column(db.Date)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    anuncio_id = db.Column(db.Integer, db.ForeignKey("anuncios.id", ondelete="CASCADE"), nullable=False)

    usuario = db.relationship("Usuario", back_populates="perguntas")
    anuncio = db.relationship("Anuncio", back_populates="perguntas")


class Compra(db.Model):
    __tablename__ = "compras"

    id = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.Date, nullable=False, default=date.today)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    valor_total = db.Column(db.Float, nullable=False)
    comprador_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    anuncio_id = db.Column(db.Integer, db.ForeignKey("anuncios.id", ondelete="CASCADE"), nullable=False)

    comprador = db.relationship("Usuario", back_populates="compras")
    anuncio = db.relationship("Anuncio", back_populates="compras")


class Favorito(db.Model):
    __tablename__ = "favoritos"
    __table_args__ = (db.UniqueConstraint("usuario_id", "anuncio_id", name="uq_favorito_usuario_anuncio"),)

    id = db.Column(db.Integer, primary_key=True)
    data_adicao = db.Column(db.Date, nullable=False, default=date.today)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    anuncio_id = db.Column(db.Integer, db.ForeignKey("anuncios.id", ondelete="CASCADE"), nullable=False)

    usuario = db.relationship("Usuario", back_populates="favoritos")
    anuncio = db.relationship("Anuncio", back_populates="favoritos")


def data_do_formulario(nome_campo):
    return datetime.strptime(request.form[nome_campo], "%Y-%m-%d").date()


def opcoes_usuarios():
    return [(usuario.id, usuario.nome) for usuario in Usuario.query.order_by(Usuario.nome).all()]


def opcoes_categorias():
    return [(categoria.id, categoria.nome) for categoria in Categoria.query.order_by(Categoria.nome).all()]


def opcoes_anuncios():
    return [(anuncio.id, anuncio.titulo) for anuncio in Anuncio.query.order_by(Anuncio.titulo).all()]


def salvar_alteracao(mensagem):
    try:
        db.session.commit()
        flash(mensagem, "sucesso")
        return True
    except IntegrityError:
        db.session.rollback()
        flash("Não foi possível salvar. Verifique se o registro já existe.", "erro")
        return False


def campos_usuario(usuario=None):
    return [
        {"name": "nome", "label": "Nome completo", "type": "text", "value": usuario.nome if usuario else "", "required": True},
        {"name": "email", "label": "E-mail", "type": "email", "value": usuario.email if usuario else "", "required": True},
        {"name": "senha", "label": "Senha" if not usuario else "Nova senha (deixe em branco para manter)", "type": "password", "value": "", "required": not usuario},
    ]


def campos_categoria(categoria=None):
    return [
        {"name": "nome", "label": "Nome da categoria", "type": "text", "value": categoria.nome if categoria else "", "required": True},
        {"name": "descricao", "label": "Descrição", "type": "textarea", "value": categoria.descricao if categoria else "", "required": True},
    ]


def campos_anuncio(anuncio=None):
    return [
        {"name": "titulo", "label": "Título", "type": "text", "value": anuncio.titulo if anuncio else "", "required": True},
        {"name": "descricao", "label": "Descrição", "type": "textarea", "value": anuncio.descricao if anuncio else "", "required": True},
        {"name": "preco", "label": "Preço", "type": "number", "step": "0.01", "min": "0.01", "value": anuncio.preco if anuncio else "", "required": True},
        {"name": "data_publicacao", "label": "Data da publicação", "type": "date", "value": anuncio.data_publicacao.isoformat() if anuncio else date.today().isoformat(), "required": True},
        {"name": "usuario_id", "label": "Anunciante", "type": "select", "value": anuncio.usuario_id if anuncio else "", "options": opcoes_usuarios(), "required": True},
        {"name": "categoria_id", "label": "Categoria", "type": "select", "value": anuncio.categoria_id if anuncio else "", "options": opcoes_categorias(), "required": True},
    ]


def campos_pergunta(pergunta=None):
    return [
        {"name": "texto", "label": "Pergunta", "type": "textarea", "value": pergunta.texto if pergunta else "", "required": True},
        {"name": "data_pergunta", "label": "Data da pergunta", "type": "date", "value": pergunta.data_pergunta.isoformat() if pergunta else date.today().isoformat(), "required": True},
        {"name": "resposta", "label": "Resposta do anunciante", "type": "textarea", "value": pergunta.resposta if pergunta and pergunta.resposta else "", "required": False},
        {"name": "data_resposta", "label": "Data da resposta", "type": "date", "value": pergunta.data_resposta.isoformat() if pergunta and pergunta.data_resposta else "", "required": False},
        {"name": "usuario_id", "label": "Usuário que perguntou", "type": "select", "value": pergunta.usuario_id if pergunta else "", "options": opcoes_usuarios(), "required": True},
        {"name": "anuncio_id", "label": "Anúncio", "type": "select", "value": pergunta.anuncio_id if pergunta else "", "options": opcoes_anuncios(), "required": True},
    ]


def campos_compra(compra=None):
    return [
        {"name": "data_compra", "label": "Data da compra", "type": "date", "value": compra.data_compra.isoformat() if compra else date.today().isoformat(), "required": True},
        {"name": "quantidade", "label": "Quantidade", "type": "number", "min": "1", "step": "1", "value": compra.quantidade if compra else 1, "required": True},
        {"name": "valor_total", "label": "Valor total", "type": "number", "min": "0.01", "step": "0.01", "value": compra.valor_total if compra else "", "required": True},
        {"name": "comprador_id", "label": "Comprador", "type": "select", "value": compra.comprador_id if compra else "", "options": opcoes_usuarios(), "required": True},
        {"name": "anuncio_id", "label": "Anúncio comprado", "type": "select", "value": compra.anuncio_id if compra else "", "options": opcoes_anuncios(), "required": True},
    ]


def campos_favorito(favorito=None):
    return [
        {"name": "data_adicao", "label": "Data da adição", "type": "date", "value": favorito.data_adicao.isoformat() if favorito else date.today().isoformat(), "required": True},
        {"name": "usuario_id", "label": "Usuário", "type": "select", "value": favorito.usuario_id if favorito else "", "options": opcoes_usuarios(), "required": True},
        {"name": "anuncio_id", "label": "Anúncio favorito", "type": "select", "value": favorito.anuncio_id if favorito else "", "options": opcoes_anuncios(), "required": True},
    ]


@app.template_filter("moeda")
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


@app.template_filter("data_br")
def formatar_data(valor):
    return valor.strftime("%d/%m/%Y") if valor else "—"


@app.route("/")
def inicio():
    totais = {
        "usuarios": Usuario.query.count(),
        "anuncios": Anuncio.query.count(),
        "compras": Compra.query.count(),
        "favoritos": Favorito.query.count(),
    }
    return render_template("index.html", totais=totais)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        email = request.form["email"].strip().lower()
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario and usuario.verificar_senha(request.form["senha"]):
            login_user(usuario, remember="lembrar" in request.form)
            flash(f"Bem-vinda, {usuario.nome}!", "sucesso")
            return redirect(url_for("inicio"))
        flash("E-mail ou senha incorretos.", "erro")

    return render_template("login.html", titulo="Entrar")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        email = request.form["email"].strip().lower()
        if Usuario.query.filter_by(email=email).first():
            flash("Este e-mail já está cadastrado.", "erro")
        else:
            usuario = Usuario(nome=request.form["nome"].strip(), email=email)
            usuario.definir_senha(request.form["senha"])
            db.session.add(usuario)
            if salvar_alteracao("Conta criada com sucesso! Agora faça o login."):
                return redirect(url_for("login"))
    return render_template("cadastro.html", titulo="Criar conta")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sessão encerrada com segurança.", "sucesso")
    return redirect(url_for("login"))


# CRUD DE USUÁRIOS
@app.route("/usuarios")
@login_required
def usuarios():
    return render_template("usuarios/lista.html", registros=Usuario.query.order_by(Usuario.id).all())


@app.route("/usuarios/novo", methods=["GET", "POST"])
@login_required
def usuario_novo():
    if request.method == "POST":
        usuario = Usuario(nome=request.form["nome"], email=request.form["email"].strip().lower())
        usuario.definir_senha(request.form["senha"])
        db.session.add(usuario)
        if salvar_alteracao("Usuário cadastrado com sucesso!"):
            return redirect(url_for("usuarios"))
    return render_template("formulario.html", titulo="Cadastrar usuário", campos=campos_usuario(), voltar="usuarios")


@app.route("/usuarios/<int:id>/editar", methods=["GET", "POST"])
@login_required
def usuario_editar(id):
    usuario = db.get_or_404(Usuario, id)
    if request.method == "POST":
        usuario.nome, usuario.email = request.form["nome"], request.form["email"].strip().lower()
        if request.form["senha"]:
            usuario.definir_senha(request.form["senha"])
        if salvar_alteracao("Usuário atualizado com sucesso!"):
            return redirect(url_for("usuarios"))
    return render_template("formulario.html", titulo="Editar usuário", campos=campos_usuario(usuario), voltar="usuarios")


@app.route("/usuarios/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def usuario_excluir(id):
    usuario = db.get_or_404(Usuario, id)
    if usuario.id == current_user.id:
        flash("Você não pode excluir o usuário que está com a sessão aberta.", "erro")
        return redirect(url_for("usuarios"))
    if request.method == "POST":
        db.session.delete(usuario)
        salvar_alteracao("Usuário excluído com sucesso!")
        return redirect(url_for("usuarios"))
    return render_template("confirmar_exclusao.html", titulo="Excluir usuário", registro=usuario.nome, voltar="usuarios")


# CRUD DE CATEGORIAS
@app.route("/categorias")
@login_required
def categorias():
    return render_template("categorias/lista.html", registros=Categoria.query.order_by(Categoria.id).all())


@app.route("/categorias/nova", methods=["GET", "POST"])
@login_required
def categoria_nova():
    if request.method == "POST":
        db.session.add(Categoria(nome=request.form["nome"], descricao=request.form["descricao"]))
        if salvar_alteracao("Categoria cadastrada com sucesso!"):
            return redirect(url_for("categorias"))
    return render_template("formulario.html", titulo="Cadastrar categoria", campos=campos_categoria(), voltar="categorias")


@app.route("/categorias/<int:id>/editar", methods=["GET", "POST"])
@login_required
def categoria_editar(id):
    categoria = db.get_or_404(Categoria, id)
    if request.method == "POST":
        categoria.nome, categoria.descricao = request.form["nome"], request.form["descricao"]
        if salvar_alteracao("Categoria atualizada com sucesso!"):
            return redirect(url_for("categorias"))
    return render_template("formulario.html", titulo="Editar categoria", campos=campos_categoria(categoria), voltar="categorias")


@app.route("/categorias/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def categoria_excluir(id):
    categoria = db.get_or_404(Categoria, id)
    if request.method == "POST":
        db.session.delete(categoria)
        salvar_alteracao("Categoria excluída com sucesso!")
        return redirect(url_for("categorias"))
    return render_template("confirmar_exclusao.html", titulo="Excluir categoria", registro=categoria.nome, voltar="categorias")


# CRUD DE ANÚNCIOS
@app.route("/anuncios")
@login_required
def anuncios():
    return render_template("anuncios/lista.html", registros=Anuncio.query.order_by(Anuncio.id).all())


@app.route("/anuncios/novo", methods=["GET", "POST"])
@login_required
def anuncio_novo():
    if request.method == "POST":
        anuncio = Anuncio(titulo=request.form["titulo"], descricao=request.form["descricao"], preco=float(request.form["preco"]), data_publicacao=data_do_formulario("data_publicacao"), usuario_id=int(request.form["usuario_id"]), categoria_id=int(request.form["categoria_id"]))
        db.session.add(anuncio)
        if salvar_alteracao("Anúncio cadastrado com sucesso!"):
            return redirect(url_for("anuncios"))
    return render_template("formulario.html", titulo="Cadastrar anúncio", campos=campos_anuncio(), voltar="anuncios")


@app.route("/anuncios/<int:id>/editar", methods=["GET", "POST"])
@login_required
def anuncio_editar(id):
    anuncio = db.get_or_404(Anuncio, id)
    if request.method == "POST":
        anuncio.titulo, anuncio.descricao = request.form["titulo"], request.form["descricao"]
        anuncio.preco, anuncio.data_publicacao = float(request.form["preco"]), data_do_formulario("data_publicacao")
        anuncio.usuario_id, anuncio.categoria_id = int(request.form["usuario_id"]), int(request.form["categoria_id"])
        if salvar_alteracao("Anúncio atualizado com sucesso!"):
            return redirect(url_for("anuncios"))
    return render_template("formulario.html", titulo="Editar anúncio", campos=campos_anuncio(anuncio), voltar="anuncios")


@app.route("/anuncios/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def anuncio_excluir(id):
    anuncio = db.get_or_404(Anuncio, id)
    if request.method == "POST":
        db.session.delete(anuncio)
        salvar_alteracao("Anúncio excluído com sucesso!")
        return redirect(url_for("anuncios"))
    return render_template("confirmar_exclusao.html", titulo="Excluir anúncio", registro=anuncio.titulo, voltar="anuncios")


# CRUD DE PERGUNTAS E RESPOSTAS
@app.route("/perguntas")
@login_required
def perguntas():
    return render_template("perguntas/lista.html", registros=Pergunta.query.order_by(Pergunta.id).all())


@app.route("/perguntas/nova", methods=["GET", "POST"])
@login_required
def pergunta_nova():
    if request.method == "POST":
        pergunta = Pergunta(texto=request.form["texto"], data_pergunta=data_do_formulario("data_pergunta"), resposta=request.form["resposta"] or None, data_resposta=data_do_formulario("data_resposta") if request.form["data_resposta"] else None, usuario_id=int(request.form["usuario_id"]), anuncio_id=int(request.form["anuncio_id"]))
        db.session.add(pergunta)
        if salvar_alteracao("Pergunta cadastrada com sucesso!"):
            return redirect(url_for("perguntas"))
    return render_template("formulario.html", titulo="Cadastrar pergunta", campos=campos_pergunta(), voltar="perguntas")


@app.route("/perguntas/<int:id>/editar", methods=["GET", "POST"])
@login_required
def pergunta_editar(id):
    pergunta = db.get_or_404(Pergunta, id)
    if request.method == "POST":
        pergunta.texto, pergunta.data_pergunta = request.form["texto"], data_do_formulario("data_pergunta")
        pergunta.resposta = request.form["resposta"] or None
        pergunta.data_resposta = data_do_formulario("data_resposta") if request.form["data_resposta"] else None
        pergunta.usuario_id, pergunta.anuncio_id = int(request.form["usuario_id"]), int(request.form["anuncio_id"])
        if salvar_alteracao("Pergunta atualizada com sucesso!"):
            return redirect(url_for("perguntas"))
    return render_template("formulario.html", titulo="Editar pergunta e resposta", campos=campos_pergunta(pergunta), voltar="perguntas")


@app.route("/perguntas/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def pergunta_excluir(id):
    pergunta = db.get_or_404(Pergunta, id)
    if request.method == "POST":
        db.session.delete(pergunta)
        salvar_alteracao("Pergunta excluída com sucesso!")
        return redirect(url_for("perguntas"))
    return render_template("confirmar_exclusao.html", titulo="Excluir pergunta", registro=pergunta.texto, voltar="perguntas")


# CRUD DE COMPRAS
@app.route("/compras")
@login_required
def compras():
    return render_template("compras/lista.html", registros=Compra.query.order_by(Compra.id).all())


@app.route("/compras/nova", methods=["GET", "POST"])
@login_required
def compra_nova():
    if request.method == "POST":
        compra = Compra(data_compra=data_do_formulario("data_compra"), quantidade=int(request.form["quantidade"]), valor_total=float(request.form["valor_total"]), comprador_id=int(request.form["comprador_id"]), anuncio_id=int(request.form["anuncio_id"]))
        db.session.add(compra)
        if salvar_alteracao("Compra cadastrada com sucesso!"):
            return redirect(url_for("compras"))
    return render_template("formulario.html", titulo="Cadastrar compra", campos=campos_compra(), voltar="compras")


@app.route("/compras/<int:id>/editar", methods=["GET", "POST"])
@login_required
def compra_editar(id):
    compra = db.get_or_404(Compra, id)
    if request.method == "POST":
        compra.data_compra, compra.quantidade = data_do_formulario("data_compra"), int(request.form["quantidade"])
        compra.valor_total, compra.comprador_id = float(request.form["valor_total"]), int(request.form["comprador_id"])
        compra.anuncio_id = int(request.form["anuncio_id"])
        if salvar_alteracao("Compra atualizada com sucesso!"):
            return redirect(url_for("compras"))
    return render_template("formulario.html", titulo="Editar compra", campos=campos_compra(compra), voltar="compras")


@app.route("/compras/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def compra_excluir(id):
    compra = db.get_or_404(Compra, id)
    if request.method == "POST":
        db.session.delete(compra)
        salvar_alteracao("Compra excluída com sucesso!")
        return redirect(url_for("compras"))
    return render_template("confirmar_exclusao.html", titulo="Excluir compra", registro=f"Compra #{compra.id}", voltar="compras")


# CRUD DE FAVORITOS
@app.route("/favoritos")
@login_required
def favoritos():
    return render_template("favoritos/lista.html", registros=Favorito.query.order_by(Favorito.id).all())


@app.route("/favoritos/novo", methods=["GET", "POST"])
@login_required
def favorito_novo():
    if request.method == "POST":
        favorito = Favorito(data_adicao=data_do_formulario("data_adicao"), usuario_id=int(request.form["usuario_id"]), anuncio_id=int(request.form["anuncio_id"]))
        db.session.add(favorito)
        if salvar_alteracao("Favorito cadastrado com sucesso!"):
            return redirect(url_for("favoritos"))
    return render_template("formulario.html", titulo="Cadastrar favorito", campos=campos_favorito(), voltar="favoritos")


@app.route("/favoritos/<int:id>/editar", methods=["GET", "POST"])
@login_required
def favorito_editar(id):
    favorito = db.get_or_404(Favorito, id)
    if request.method == "POST":
        favorito.data_adicao = data_do_formulario("data_adicao")
        favorito.usuario_id, favorito.anuncio_id = int(request.form["usuario_id"]), int(request.form["anuncio_id"])
        if salvar_alteracao("Favorito atualizado com sucesso!"):
            return redirect(url_for("favoritos"))
    return render_template("formulario.html", titulo="Editar favorito", campos=campos_favorito(favorito), voltar="favoritos")


@app.route("/favoritos/<int:id>/excluir", methods=["GET", "POST"])
@login_required
def favorito_excluir(id):
    favorito = db.get_or_404(Favorito, id)
    if request.method == "POST":
        db.session.delete(favorito)
        salvar_alteracao("Favorito excluído com sucesso!")
        return redirect(url_for("favoritos"))
    return render_template("confirmar_exclusao.html", titulo="Excluir favorito", registro=favorito.anuncio.titulo, voltar="favoritos")


@app.route("/relatorios/compras")
@login_required
def relatorio_compras():
    registros = Compra.query.order_by(Compra.data_compra.desc()).all()
    return render_template("relatorio.html", titulo="Relatório de compras", pessoa_label="Comprador", registros=registros, total=sum(item.valor_total for item in registros), tipo="compras")


@app.route("/relatorios/vendas")
@login_required
def relatorio_vendas():
    registros = Compra.query.order_by(Compra.data_compra.desc()).all()
    return render_template("relatorio.html", titulo="Relatório de vendas", pessoa_label="Vendedor", registros=registros, total=sum(item.valor_total for item in registros), tipo="vendas")


def criar_dados_iniciais():
    if Usuario.query.count() > 0:
        return

    anna = Usuario(nome="Anna Julia Torres Martins de Deus", email="anna@email.com")
    marina = Usuario(nome="Marina Costa", email="marina@email.com")
    lucas = Usuario(nome="Lucas Lima", email="lucas@email.com")
    for usuario in (anna, marina, lucas):
        usuario.definir_senha("123456")
    eletronicos = Categoria(nome="Eletrônicos", descricao="Celulares, notebooks e acessórios")
    casa = Categoria(nome="Casa e decoração", descricao="Itens para todos os ambientes")
    livros = Categoria(nome="Livros", descricao="Livros novos e usados")
    db.session.add_all([anna, marina, lucas, eletronicos, casa, livros])
    db.session.flush()

    fone = Anuncio(titulo="Fone Bluetooth", descricao="Fone sem fio com estojo carregador.", preco=129.90, data_publicacao=date(2026, 8, 2), usuario=anna, categoria=eletronicos)
    luminaria = Anuncio(titulo="Luminária de mesa", descricao="Luminária articulada para estudo.", preco=79.00, data_publicacao=date(2026, 8, 3), usuario=lucas, categoria=casa)
    livro = Anuncio(titulo="Livro de Python", descricao="Livro introdutório em ótimo estado.", preco=65.00, data_publicacao=date(2026, 8, 4), usuario=marina, categoria=livros)
    db.session.add_all([fone, luminaria, livro])
    db.session.flush()

    db.session.add_all([
        Pergunta(texto="O produto possui garantia?", data_pergunta=date(2026, 8, 5), resposta="Sim, possui garantia de 90 dias.", data_resposta=date(2026, 8, 5), usuario=marina, anuncio=fone),
        Pergunta(texto="Você envia para outro estado?", data_pergunta=date(2026, 8, 6), usuario=anna, anuncio=livro),
        Compra(data_compra=date(2026, 8, 7), quantidade=1, valor_total=129.90, comprador=marina, anuncio=fone),
        Favorito(data_adicao=date(2026, 8, 6), usuario=anna, anuncio=livro),
    ])
    db.session.commit()


def proteger_senhas_antigas():
    """Converte as senhas da Trilha 2 para hashes sem apagar o banco existente."""
    alterou = False
    for usuario in Usuario.query.all():
        if not usuario.senha.startswith(("scrypt:", "pbkdf2:")):
            usuario.definir_senha(usuario.senha)
            alterou = True
    if alterou:
        db.session.commit()


with app.app_context():
    db.create_all()
    criar_dados_iniciais()
    proteger_senhas_antigas()


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
