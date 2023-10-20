import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from Database.db import get_db

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/', methods=('GET', 'POST'))
def product():
    if request.method == 'GET':
        db=get_db()
        items=db.execute("SELECT * FROM Product").fetchall()
        return render_template('product/products.html',products=items,title="Merch Store")