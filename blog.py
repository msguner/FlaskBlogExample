# -*- coding: utf-8 -*-

from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from forms import RegisterForm

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

# mysql config
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASS"] = ""
app.config["MYSQL_DB"] = "flask_blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == "POST" and form.validate:
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()
        sorgu = "INSERT into users(name,username,email,password) VALUES(%s, %s, %s, %s)" % (name,username,email,password)
        cursor.execute(sorgu)
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("index"))
    
    return render_template("register.html", form=form)

@app.route("/article/<string:id>")
def articleDetail(id):
    return "Article id: " + id





if __name__ == "__main__":
    app.run(debug=True)