from flask import Flask, render_template, redirect, url_for, make_response, jsonify
from data import db_session, jobs_api
from data.users import User
from data.jobs import Job
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, EmailField, BooleanField, DateTimeField
from wtforms.validators import DataRequired
import hashlib
from flask_login import LoginManager, login_user, logout_user, current_user

db_session.global_init('db/database.db')
session = db_session.create_session()

login_manager = LoginManager()

app = Flask(__name__)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(int(user_id))


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


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Login')


class JobForm(FlaskForm):
    job = StringField('Description', validators=[DataRequired()])
    work_size = DecimalField('Work size (hours)', validators=[DataRequired()])
    team_leader = DecimalField('Team leader id', validators=[DataRequired()])
    collaborators = StringField(
        'Collaborator ids', validators=[DataRequired()])
    is_finished = BooleanField(
        'Is already finished')
    submit = SubmitField('Add job')


def custom_render(name: str, **params):
    params['style_url'] = url_for('static', filename='css/main.css')
    return render_template(name, **params)


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = session.query(Job).all()
    return custom_render('index.html', works=jobs)


@app.route('/success')
def success():
    return custom_render('success.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
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

        login_user(user)

        return redirect('/')
    params = {'form': form}
    return custom_render('register.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        params = {'message': 'Incorrect login or password', 'form': form}
        return custom_render('login.html', **params)
    return custom_render('login.html', form=form)


@app.route('/add-job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        job = Job()
        job.job = form.job.data
        job.work_size = int(form.work_size.data)
        job.team_leader = int(form.team_leader.data)
        job.collaborators = form.collaborators.data
        job.is_finished = bool(form.is_finished.data)
        session.add(job)
        session.commit()
        return redirect('/')

    params = {'form': form}
    return custom_render('add_job.html', **params)


@app.route('/edit-job/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id: int):
    form = JobForm()
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if form.validate_on_submit():
        if not job:
            return make_response(jsonify({"error":  "Not found"}), 400)
        if not current_user.is_authenticated:
            return make_response(jsonify({'error': 'Unauthorized'}), 401)
        team_leader = job.team_leader
        if current_user.id != 1 and current_user.id != team_leader:
            return make_response(jsonify({'error': 'Not enough privileges'}), 403)
        job.job = form.job.data
        job.work_size = int(form.work_size.data)
        job.team_leader = int(form.team_leader.data)
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        session.commit()
        return redirect('/')
    return custom_render('edit_job.html', job_id=job.id, form=form)


@app.route('/remove-job/<int:job_id>')
def remove_job(job_id: int):
    session = db_session.create_session()
    job = session.query(Job).get(job_id)
    if not job:
        return make_response(jsonify({"error":  "Not found"}), 400)
    if not current_user.is_authenticated:
        return make_response(jsonify({'error': 'Unauthorized'}), 401)
    team_leader = job.team_leader
    if current_user.id != 1 and current_user.id != team_leader:
        return make_response(jsonify({'error': 'Not enough privileges'}), 403)
    session.delete(job)
    session.commit()
    return redirect('/')


@app.route('/job-added-successfully')
def job_added_successfully():
    return custom_render('added_successfully.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.errorhandler(400)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')
