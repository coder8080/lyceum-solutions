from flask import Flask, render_template, redirect, url_for
from sqlalchemy.orm import Session
from data import db_session
from data.users import User
from data.jobs import Job
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import hashlib

db_session.global_init('db/database.db')
session = db_session.create_session()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aoh;jlknsdg;oihkl'


class RegiterForm(FlaskForm):
    username = StringField('Login / email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    age = DecimalField('Age', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    speciality = StringField('Speciality', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')


def custom_render(name: str, **params):
    params['style_url'] = url_for('static', filename='css/main.css')
    return render_template(name, **params)


@app.route('/')
@app.route('/index')
def index():
    return custom_render('index.html')


@app.route('/success')
def success():
    return custom_render('success.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegiterForm()
    if form.validate_on_submit():
        print('validation successful')

        user = User()
        user.email = form.username.data
        user.hashed_password = hashlib.sha256(
            form.password.data.encode('utf-8')).hexdigest()
        user.surname = form.surname.data
        user.name = form.name.data
        user.age = int(form.age.data)
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data

        session.add(user)
        session.commit()

        print('adding user to database successful')

        return redirect('/success')
    params = {'form': form}
    return custom_render('register.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
