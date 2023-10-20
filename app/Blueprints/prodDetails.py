import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from Database.db import get_db

bp = Blueprint('prodDetails', __name__, url_prefix='/prodDetails')

@bp.route('/product', methods=('GET', 'POST'))
def product():
    if request.method == 'GET':
        return render_template('product/productDetails.html',title="Product Details")