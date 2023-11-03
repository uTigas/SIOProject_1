import functools
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from Database.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':

        db = get_db()
        error = []

        username = request.form['username']
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        rpass = request.form['passwordrepeat']

        if not username:
            error += ['Username is required.\n']
        if not password:
            error += ['Password is required.\n']
        if not name:
            error += ['Name is required.\n']
        if not age:
            error += ['Age is required.\n']
        if not phone:
            error += ['Phone is required.\n']
        if not email:
            error += ['Email is required.\n']
        if not rpass == password:
            error += ['Passwords dont match.\n']

        if len(error) == 0:
            if not password_strong(password):
                error+=[("Password must be a mix of uppercase and lowercase letters, have at least one digit, at least one special character from the specified set, and a minimum length of 8 characters.","danger")]
            else:
                try:
                    db.execute(
                        "INSERT INTO User (Username, Password, Name , PhoneNumber , Email , Age , Role) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (username, generate_password_hash(password) , name , phone , email , age , 'user')
                    )
                    db.commit()
                except db.IntegrityError:
                    error += [f"User {username} is already registered."]
                else:
                    return redirect(url_for("auth.login"))
            
        for m in error:
            flash(m,'danger')

    return render_template('auth/register.html',title="Register")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        error = None

        user = db.execute(
            'SELECT * FROM user WHERE Username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['Password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['ID']
            
            return redirect(url_for('index'))

        flash(error,'danger')


    return render_template('auth/login.html')

@bp.route('/change_password', methods=('GET', 'POST'))
def change_password():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        npassword = request.form['passwordnew']
        rpass = request.form['passwordrepeat']

        db = get_db()
        error = []

        if not rpass == npassword:
            error += ['Passwords dont match.\n']

        user = db.execute(
            'SELECT * FROM user WHERE Username = ?', (username,)
        ).fetchone()

        if user is None:
            error += ['Incorrect username.']
        elif not check_password_hash(user['Password'], password):
            error += ['Incorrect password.']

        if len(error) == 0:
            if not password_strong(npassword):
                error+=[("Password must be a mix of uppercase and lowercase letters, have at least one digit, at least one special character from the specified set, and a minimum length of 8 characters.","danger")]
            else:
                try:
                    db.execute(
                        "Update User SET Password=(?) WHERE Username = (?) ",
                        (generate_password_hash(npassword),username)
                    )
                    db.commit()

                    return redirect(url_for('auth.login'))
                
                except db.IntegrityError:
                    error += [f"ERROR:Unreachable code"]

        for m in error:
            flash(m,'danger')

    return render_template('auth/change_password.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view

def password_strong(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&!])[A-Za-z\d@#$%^&!]{8,}$'
    return re.match(pattern, password) is not None