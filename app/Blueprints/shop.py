from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Blueprints.auth import login_required
from Database.db import get_db

bp = Blueprint('shop', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/productDetails/<name>')
def productDetails(name):
    db=get_db()
    try:
        query=db.execute( "SELECT * FROM Product WHERE Name=?",(name,))
        query=query.fetchall()
        if len(query)==0:
            flash(f"Product {name} does not exist.",'danger')
            return products()  
    except db.IntegrityError:
        flash(f"Product {name} does not exist.",'danger')
        return products()  
    else:
        flash("Item successfully added to the Cart!","info")
        
    return render_template('product/productDetails.html',size=True,color=True,name=query[0][0],description=query[0][1],price=query[0][3],image="https://img.freepik.com/fotos-premium/o-suricato-suricata-suricatta-ou-suricate-e-um-pequeno-mangusto-encontrado-no-sul-da-africa_208861-941.jpg")


@bp.route('/products', methods=('GET', 'POST'))
def products():
    if request.method == 'GET':
        db=get_db()
        items=db.execute("SELECT * FROM Product").fetchall()
        return render_template('product/products.html',products=items,title="Merch Store")
    
@bp.route('/whishlist')
def whishlist():
    return render_template('whishlist.html')