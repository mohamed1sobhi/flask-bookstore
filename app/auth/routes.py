from flask import Blueprint
from flask import render_template, redirect, url_for
from flask_login import login_user
from app.models import User
from app.auth.forms import RegisterForm,LoginForm

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register',methods=['GET','POST'],endpoint='register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data, 
            last_name=form.last_name.data, 
            email=form.email.data,
            password=form.password.data
        )
        user.save_to_db()
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)



@auth_blueprint.route('/login', methods=['GET', 'POST'],endpoint='login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            return redirect(url_for('main.books'))
    
    return render_template('auth/login.html', form=form)

