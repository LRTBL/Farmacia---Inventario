from flask import Flask, render_template, request, redirect , url_for , session, g
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'bavn9227'
app.config['MYSQL_PASSWORD'] = 'Benjamin271999'
app.config['MYSQL_DB'] = 'farmaciainvent'

app.secret_key = "12345"

mysql = MySQL(app)

@app.route("/" , methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session.pop('username', None)
        username = str(request.form["user"])
        password = str(request.form["password"])
        cursor = mysql.connection.cursor()
        cursor.execute("select * from usuario where nombreUsuario = %s and contraseña = %s  ", (username, password))
        data = cursor.fetchall()
        if len(data) == 1:
            session["username"] = username
            return redirect(url_for("home"))
    return render_template("index.html", title="Sign Up")

@app.route("/logout")
def logOut():
    session.pop("username", None)
    return render_template("index.html", title="Sign Up")

@app.route("/home")
def home():
    if g.username:
        return render_template("home.html", user= session["username"])
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']

@app.route("/users")
def users():
    return render_template("usuarios.html")


@app.route("/inventory")
def inventory():
    return render_template("inventario.html")

@app.route("/recepcion")
def recepcion():
    return render_template("recepcion.html")

if __name__ == '__main__':
    app.run(port = 3000 , debug = True)

