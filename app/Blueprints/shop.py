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
        query=query.fetchone()
        if len(query)==0:
            flash(f"Product {name} does not exist.",'danger')
            return products()  
        category=db.execute("Select CName from Category_Has_Product WHERE PName=?",(query[0],)).fetchone()
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
                
    avg = db.execute("SELECT AVG(Score) as avg FROM Review WHERE PName = ? GROUP BY PName",(name,)).fetchone()

    return render_template('product/productDetails.html',
                           name=name,images=images,
                           category=category[0],
                           size=True,
                           color=True,
                           product=query,
                           reviews=db.execute("SELECT * FROM Review WHERE PName = ?",(name,)).fetchall(),
                           avg=int(avg['avg']*100)/100,
                           title="Product - " + name)


@bp.route('/products', methods=('GET', 'POST'))
def products():
    images=dict()
    db=get_db()

    category = None
    minPrice = None
    maxPrice = None
    search = None
    error = []

    if request.method == 'GET':
        category = request.args.get("category")
        minPrice = request.args.get("minPrice")
        maxPrice = request.args.get("maxPrice")
        search = request.args.get("input")

    if request.method=="POST":
        category = request.form.get("category")
        minPrice = request.form.get("minPrice")
        maxPrice = request.form.get("maxPrice")
        search = request.form.get("input")

    MIN_PRICE = int(db.execute("SELECT MIN(price) AS min_price FROM Product").fetchone()["min_price"])
    MAX_PRICE = int(db.execute("SELECT MAX(price) AS max_price FROM Product").fetchone()["max_price"])

    if minPrice is None:
        minPrice = MIN_PRICE

    if maxPrice is None:
        maxPrice = MAX_PRICE

    if search is None:
        search = ""
    search=search

    try:
        maxPrice = int(maxPrice)
        minPrice = int(minPrice)
    except:
        minPrice = MIN_PRICE
        maxPrice = MAX_PRICE
        error += ["Invalid price"]

    if minPrice > maxPrice:
        minPrice = MIN_PRICE
        maxPrice = MAX_PRICE
        error += ["Minimum price bigger than maximum price."]

    if request.method=="POST":
        return redirect( url_for('shop.products', minPrice=minPrice,maxPrice=maxPrice,input=search,category=category) )
     
    search = "%" + search + "%"
    if category is None or len(category)==0 or category=="All" or category=="None":   
        items=db.execute("SELECT * FROM Product Where Price >= ? AND Price <= ? and Product.Name LIKE ? ",(minPrice,maxPrice,search,)).fetchall()
        category="All"
    else:
        items=db.execute("SELECT * FROM Product JOIN Category_Has_Product ON Cname=? WHERE Pname=Product.Name and Price >= ? AND Price <= ? and Product.Name LIKE ?",(category,minPrice,maxPrice,search,)).fetchall()


    categories=db.execute("SELECT * FROM Category").fetchall()

    for item in items:
        images[item[0]]=db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?",(item[0],)).fetchone()

    for m in error:
            flash(m,'danger')

    return render_template('product/products.html',
                               search=search[1:-1],
                               categories=categories, 
                               products=items,
                               title="Merch Store",
                               images=images,
                               category=category,
                               MIN_PRICE=MIN_PRICE,
                               MAX_PRICE=MAX_PRICE,
                               minPrice=minPrice,
                               maxPrice=maxPrice)


@bp.route('/wishlist',methods=("GET","POST"))
@login_required
def wishlist():
        images=dict()
        items=[]
        db=get_db()
        
        if request.method =="POST":
            db.execute("DELETE FROM Wishlist Where Client=? AND Pname=?",(g.user["Username"],request.form.get("product"),))
            db.commit()
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
        score = request.form['score']

        if len(review) == 0:
            error += ["Empty review"]

        try:
            score = int(score)
            if score is None or score > 5 or score < 0:
                error += ["Invalid score"]
        except:
            error += ["Invalid score"]
            
        if len(error) == 0:
            try:
                db.execute(
                    "INSERT INTO Review (Author,PName, ReviewBody,Score) VALUES (?, ?, ?, ?)",
                    (g.user['Username'],name,review,score)
                )
                db.commit()
            except db.IntegrityError:
                error += [f"Product {name} doesnt exist."]
            else:
                return redirect(url_for("shop.productDetails",name=name))
            
        for m in error:
            flash(m,'danger')

    return [dict(row) for row in db.execute("SELECT * FROM Review WHERE PName = ?",(name,)).fetchall()]
    
@bp.route("/cart",methods=("GET","POST"))
@login_required
def cart():
    return render_template("buy/cart.html")