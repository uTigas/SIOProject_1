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

@bp.route('/productDetails/<name>', methods=('GET', 'POST'))
def productDetails(name):
    db=get_db()
    try:
        query=db.execute( "SELECT * FROM Product WHERE Name=?",(name,))
        query=query.fetchall()
        if len(query)==0:
            flash(f"Product {name} does not exist.",'danger')
            return products()  
        category=db.execute("Select CName from Category_Has_Product WHERE PName=?",(query[0][0],)).fetchone()
        images=db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?",(name,)).fetchall()

    except db.IntegrityError:
        flash(f"Product {name} does not exist.",'danger')
        return products()  
    if request.method=="POST":
        if request.form.get("cart"):
            flash("Item successfully added to the Cart!","info")
        else:
            try:
                db.execute(
                    "INSERT INTO Wishlist (Client, Pname) VALUES (?, ?)",
                    (g.user['Username'],name)
                )
                db.commit()
                flash("Item successfully added to the Wishlist!","info")
            except db.IntegrityError:
                flash("Item already in Wishlist!","info")

    return render_template('product/productDetails.html',images=images,category=category[0],size=True,color=True,name=query[0][0],description=query[0][1],price=query[0][2],reviews=db.execute("SELECT * FROM Review WHERE PName = ?",(name,)).fetchall())


@bp.route('/products', methods=('GET', 'POST'))
def products():
    if request.method == 'GET':
        images=dict()
        db=get_db()
        if request.args.get("category")==None:   
            items=db.execute("SELECT * FROM Product").fetchall()
            categories=db.execute("SELECT * FROM Category").fetchall()
            category="All"
        else:
            items=db.execute("SELECT * FROM Product JOIN Category_Has_Product ON Cname=? WHERE Pname=Product.Name",(request.args.get("category"),)).fetchall()
            categories=db.execute("SELECT * FROM Category").fetchall()
            category=request.args.get("category")   
        for item in items:
            images[item[0]]=db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?",(item[0],)).fetchone()
           
        return render_template('product/products.html',images=images, search="", category=category,categories=categories, products=items,title="Merch Store")
   
    if request.method=="POST":
        db=get_db()
        items = db.execute("SELECT * FROM Product WHERE Product.Name LIKE ?",
                  (f"%{request.form.get('input')}%",)).fetchall()       
        categories=db.execute("SELECT * FROM Category").fetchall()
        return render_template('product/products.html',search=request.form.get("input"),categories=categories, products=items,title="Merch Store")


@bp.route('/wishlist')
@login_required
def wishlist():
    if request.method == 'GET':
        images=dict()
        items=[]
        db=get_db()
        products=db.execute("SELECT * FROM Wishlist Where Client=?",(g.user['Username'] ,)).fetchall()
        for p in products:
            items.append(db.execute("SELECT * FROM Product Where Name=?",(p[1],)).fetchall())
        for item in items:
            images[item[0][0]] = db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?", (item[0][0],)).fetchone()
           
        return render_template('wishlist.html',images=images, products=items,title="Wishlist")
   

@bp.route('/productDetails/<name>/review',methods=('GET', 'POST'))
@login_required
def review(name):
    error = []
    db=get_db()
    if request.method == 'POST':
        review = request.form['userReview']

        if len(review) == 0:
            error += ["Empty review"]

        if len(error) == 0:
            try:
                db.execute(
                    "INSERT INTO Review (Author,PName, ReviewBody) VALUES (?, ?, ?)",
                    (g.user['Username'],name,review)
                )
                db.commit()
            except db.IntegrityError:
                error += [f"Product {name} doesnt exist."]
            else:
                return redirect(url_for("shop.productDetails",name=name))
            
        for m in error:
            flash(m,'danger')

    return [dict(row) for row in db.execute("SELECT * FROM Review WHERE PName = ?",(name,)).fetchall()]
    
    