from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,validators
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegisterForm(FlaskForm):
    name = StringField('İsim-Soyisim :',validators=[
        Length(min=5, max=25, message="5 ile 35 karakter arasında bir isim giriniz.")
    ])
    username = StringField('Kullanıcı adı :',validators=[
        Length(min=5, max=35, message="5 ile 35 karakter arasında bir kullanıcı adı giriniz."), 
        DataRequired("Lütfen kullanıcı adını boş bırakmayın.")
    ])
    email = StringField('Email adresi :',validators=[
        Email("Lütfen geçerli bir mail adresi giriniz.")
    ])
    password = PasswordField('Parola :',validators=[
        DataRequired(message="Lütfen parolayı boş bırakmayınız."),
        EqualTo(fieldname="confirm_password", message="Parolalarınız uyuşmuyor.")
    ])
    confirm_password = PasswordField("Parola doğrula :")