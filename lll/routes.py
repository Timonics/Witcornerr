from lll import app, db
from flask import render_template, redirect, url_for, flash
from lll.forms import RegisterForm, LoginForm
from lll.models import User


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/Login')
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:  # If no errors are there
        for err_msg in form.errors.values():
            flash(f'You encountered an error: {err_msg}', category='danger')

    return render_template('register.html', form=form)
