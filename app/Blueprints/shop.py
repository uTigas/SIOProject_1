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
        category=db.execute("Select CName from Category_Has_Product WHERE PName=?",(query[0][0],)).fetchone()

    except db.IntegrityError:
        flash(f"Product {name} does not exist.",'danger')
        return products()  
    if request.method=="POST":
        flash("Item successfully added to the Cart!","info")
        
    return render_template('product/productDetails.html',category=category[0],size=True,color=True,name=query[0][0],description=query[0][1],price=query[0][2],image="https://img.freepik.com/fotos-premium/o-suricato-suricata-suricatta-ou-suricate-e-um-pequeno-mangusto-encontrado-no-sul-da-africa_208861-941.jpg")


@bp.route('/products', methods=('GET', 'POST'))
def products():
    if request.method == 'GET':
        db=get_db()
        if request.args.get("category")==None:   
            items=db.execute("SELECT * FROM Product").fetchall()
            categories=db.execute("SELECT * FROM Category").fetchall()
            category="All"
        else:
            items=db.execute("SELECT * FROM Product JOIN Category_Has_Product ON Cname=? WHERE Pname=Product.Name",(request.args.get("category"),)).fetchall()
            categories=db.execute("SELECT * FROM Category").fetchall()
            category=request.args.get("category")   

        return render_template('product/products.html',search="", category=category,categories=categories, products=items,title="Merch Store")
   
    if request.method=="POST":
        db=get_db()
        items = db.execute("SELECT * FROM Product WHERE Product.Name LIKE ?",
                  (f"%{request.form.get('input')}%",)).fetchall()       
        categories=db.execute("SELECT * FROM Category").fetchall()
        return render_template('product/products.html',search=request.form.get("input"),categories=categories, products=items,title="Merch Store")


@bp.route('/whishlist')
def whishlist():
    return render_template('whishlist.html')