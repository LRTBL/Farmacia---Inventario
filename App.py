from flask import Flask, render_template, request, redirect , url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'farmacia_inventario'

mysql = MySQL(app)

# con = MySQLdb.connect(host="", user="", password="", db="");


@app.route("/")
def Index():
    return render_template("index.html", title="sign Up")


@app.route("/checkUser", methods=["POST"])
def check():
    username = str(request.form["user"])
    password = str(request.form["password"])
    cursor = conn.cursor()
    cursor.execute("")
    user = cursor.fetchone()



    

if __name__ == '__main__':
    app.run(port = 3000 , debug = True)

