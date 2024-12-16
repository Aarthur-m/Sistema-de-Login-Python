from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from database import create_table

app = Flask(__name__)
app.config.from_object('config.Config')

# Garantir que a tabela seja criada antes de qualquer requisição


#with app.app_context():
#    create_table()  # Criar a tabela antes de iniciar o Flask

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    if request.method == "POST":

        create_table()
        usuarioForm = request.form.get("A")
        emailForm = request.form.get("B")
        senhaForm = request.form.get("C")

        senhaHash = generate_password_hash(senhaForm)

        
        # Conectar ao banco de dados
        conn = sqlite3.connect("SistemaDeusuarios.db")
        cursor = conn.cursor()

        # Verificar se o email já está registrado
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (emailForm,))
        user = cursor.fetchone()
        if user:
            conn.close()
            flash("Este Email já está registrado", "error")
            return redirect(url_for("index"))

        # Inserir o novo usuário
        cursor.execute("INSERT INTO usuarios(usuario, email, senha) VALUES (?, ?, ?)", (usuarioForm, emailForm, senhaHash))
        conn.commit()

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("index"))

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        create_table()
        emailLogin = request.form.get("D")
        senhaLogin = request.form.get("E")

        # Conectar ao banco de dados
        conn = sqlite3.connect("SistemaDeusuarios.db")
        cursor = conn.cursor()

        # Verificar se o email existe no banco
        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (emailLogin,))
        user = cursor.fetchone()

        if user:
            if check_password_hash(user[3], senhaLogin):  # user[3] é a senha
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for("index"))
            else:
                flash("Email ou senha incorretos!", "error")
                return redirect(url_for("index"))
        else:
            flash("Usuário não encontrado", "error")
            return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
