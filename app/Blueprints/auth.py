import functools

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
            try:
                db.execute(
                    "INSERT INTO user (Username, Password, Name , PhoneNumber , Email , Age , Role) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (username, generate_password_hash(password) , name , phone , email , age , 'user')
                )
                db.commit()
            except db.IntegrityError:
                error += [f"User {username} is already registered."]
            else:
                return redirect(url_for("auth.login"))
            
        for m in error:
            flash(m)

    return render_template('auth/register.html',title="Register")

@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html',title="Login")