# -*- coding: utf-8 -*-

from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from passlib.hash import sha256_crypt
from forms import RegisterForm
import myconnutils

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

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

        print ("name: %s, username: %s, email: %s, password: %s" % (name,username,email,password))
        
        try:
            with myconnutils.DBase() as db:
                # user registiration
                sql1 = "INSERT into use(name,username,email,password) VALUES(%s, %s, %s, %s)" 
                db.query(sql1, (name,username,email,password))
                db.conn.commit()

                flash(u'Kayıt işlemi başarıyla gerçekleştirildi.', 'success')
                return redirect(url_for("index"))
        except:
            flash(u'Kayıt işlemi yapılamadı.', 'danger')

    return render_template("register.html", form=form)

@app.route("/article/<string:id>")
def articleDetail(id):
    return "Article id: " + id




if __name__ == "__main__":
    app.run(debug=True)