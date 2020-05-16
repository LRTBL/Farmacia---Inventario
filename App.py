from flask import Flask, render_template, request, redirect , url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Lerietbool999'
app.config['MYSQL_DB'] = 'farmacia_inventario'
mysql = MySQL(app)

@app.route("/")
def Index():
    return render_template("index.html", title="sign Up")

@app.route("/checkUser", methods=["POST"])
def check():
    username = str(request.form["user"])
    password = str(request.form["password"])
    cursor = mysql.connection.cursor()
    cursor.execute("select * from usuario where nombreUsuario = %s and contraseña = %s  ", (username, password))
    data = cursor.fetchall()
    if len(data) == 1:
        return redirect(url_for("home"))
    else:
        return "Failed"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/users")
def users():
    return render_template("usuarios.html")


@app.route("/inventory")
def inventory():
    return render_template("inventario.html")



    

if __name__ == '__main__':
    app.run(port = 3000 , debug = True)

