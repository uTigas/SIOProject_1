from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from Blueprints.auth import login_required
from Database.db import get_db
import datetime

bp = Blueprint('shop', __name__)

@bp.route('/')
def index():
    return render_template('index.html',title="Home")

@bp.route('/productDetails/<name>', methods=('GET', 'POST'))
def productDetails(name):
    db=get_db()
    try:
        query=db.execute( "SELECT * FROM Product WHERE Name=?",(name,))
        query=query.fetchone()
        if query is None:
            flash(f"Product {name} does not exist.",'danger')
            return products()  
        category=db.execute("Select CName from Category_Has_Product WHERE PName=?",(query[0],)).fetchone()
        images=db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?",(name,)).fetchall()

    except db.IntegrityError:
        flash(f"Product {name} does not exist.",'danger')
        return products()  
    
    if request.method=="POST":
            if request.form.get("type")=="cart":
                try:
                    db.execute(
                        "INSERT INTO Cart (Client, Pname,Qty) VALUES (?, ?,?)",
                        (g.user['Username'],name,request.form.get("qty"))
                    )
                    db.commit()
                    flash("Item successfully added to the Cart!","info")
                except db.IntegrityError:
                    flash("Item already in Cart!","danger")
                except TypeError:
                    return redirect(url_for('auth.login'))
            elif request.form.get("type")=="wish":
                try:
                    db.execute(
                        "INSERT INTO Wishlist (Client, Pname) VALUES (?, ?)",
                        (g.user['Username'],name)
                    )
                    db.commit()
                    flash("Item successfully added to the Wishlist!","info")
                except db.IntegrityError:
                    flash("Item already in Wishlist!","danger")
                except TypeError:
                    return redirect(url_for('auth.login'))
            elif request.form.get("type")=="admin":
                try:
                    if request.form.get("option")=="plus":
                        db.execute("UPDATE Product SET Qty = Qty + ? WHERE [Name] = ?",(request.form.get("qty"),name))
                        db.commit()
                    elif request.form.get("option")=="minus":                
                        db.execute("UPDATE Product SET Qty = Qty - ? WHERE [Name] = ?",(request.form.get("qty"),name))
                        db.commit()
                    flash("Inventory Changed with Sucess!","info")
                except db.IntegrityError:
                    flash("Inventory management failed...","danger")
                except TypeError:
                    return redirect(url_for('auth.login'))
                return redirect(url_for("shop.productDetails",name=name))

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

    if request.method=="POST" or len(error)>0:
        for m in error:
                flash(m,'danger')
        return redirect( url_for('shop.products', minPrice=minPrice,maxPrice=maxPrice,input=search,category=category) )
     
    search = "%" + search + "%"
    # if category is None or len(category)==0 or category=="All" or category=="None":   
    #     items=db.execute("SELECT * FROM Product Where Price >= ? AND Price <= ? and Product.Name LIKE ? ",(minPrice,maxPrice,search,)).fetchall()
    #     category="All"
    # else:
    #     items=db.execute("SELECT * FROM Product JOIN Category_Has_Product ON Cname=? WHERE Pname=Product.Name and Price >= ? AND Price <= ? and Product.Name LIKE ?",
    #                      (category,minPrice,maxPrice,search,)).fetchall()
    
    if category is None or len(category)==0 or category=="All" or category=="None":
        items=db.execute("SELECT * FROM Product Where Price >=" + str(minPrice) + 
                         " AND Price <="+str(maxPrice)+
                         " AND Product.Name LIKE '"+search+"'").fetchall()
        category="All"
    else:
        items=db.execute("SELECT * FROM Product JOIN Category_Has_Product ON Cname='"+category+"' WHERE Pname=Product.Name"+
                         " AND Price >=" + str(minPrice) + 
                         " AND Price <=" + str(maxPrice)+
                         " AND Product.Name LIKE '"+search+"'").fetchall()



    categories=db.execute("SELECT * FROM Category").fetchall()

    for item in items:
        images[item[0]]=db.execute("SELECT * FROM Image JOIN Product_Has_Image ON Product_Has_Image.ID=Image.ID WHERE Pname=?",(item[0],)).fetchone()

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
    db=get_db()
    error=[]
    if request.method == 'GET':
        try:
            cart=dict()
            cart["items"] = db.execute("SELECT Cart.Pname,Description,Price,Link,Cart.Qty FROM Cart JOIN Product_Has_Image ON Product_Has_Image.Pname=Cart.Pname JOIN Image ON Product_Has_Image.ID=Image.ID JOIN Product ON Cart.Pname=Name WHERE Client=? GROUP BY Cart.Pname, Description,Cart.Qty, Price",(g.user['Username'],)).fetchall()
            cart["numItems"]=len(cart["items"])
            cart["total"]=db.execute("SELECT c.Client, SUM(p.Price * c.Qty) AS TotalPrice FROM Cart c JOIN Product p ON c.PName = p.Name WHERE c.Client = ? GROUP BY c.Client;",(g.user['Username'],)).fetchone()["TotalPrice"]
        except:
            cart=dict()
            cart["items"]=[]
            cart["total"]=0
            cart["numItems"]=0

    if request.method == 'POST':
        try:
            form = request.form
            if form["form_name"] == "checkout":
                recipt = dict()
                current_datetime = datetime.datetime.now()
                recipt["date"] = current_datetime.strftime("%d/%m/%Y %H:%M")

                recipt["total"] = float(form["total"])
                recipt["shipping"] = float(form["shipping"])

                if len(error) == 0:                    
                    items = db.execute("SELECT Pname, Qty FROM Cart WHERE Client=?", (g.user["Username"],)).fetchall()
                    for item in items:
                        maxQty=db.execute("SELECT Qty FROM Product WHERE Name=?",(item["Pname"],)).fetchone()["Qty"]
                        if maxQty<item["Qty"]:
                            error += ["Product quantity bigger than stock. " + item["Pname"]]
                            raise Exception
                    db.execute("INSERT INTO [Order] (Client, Date, ConcDate, Description,TotalPrice) VALUES (?, ?, null, ?, ?)",
                            (g.user['Username'], recipt["date"], "Awesome buy!",recipt["total"]))
                    db.commit()
                    orderID = db.execute("SELECT last_insert_rowid()").fetchone()
                    for item in items:
                        db.execute("INSERT INTO Order_Has_Product ([Order], Pname, Qty) VALUES (?, ?, ?)",
                                (orderID[0], item["Pname"], item["Qty"],))
                        db.commit()
                    db.execute("DELETE FROM Cart WHERE Client=?", (g.user['Username'],))
                    db.commit()
                    for item in items:  
                        db.execute("UPDATE Product SET Qty=Qty-? WHERE Name=?",(item["Qty"],item["Pname"],))
                    db.commit()
                    return render_template("/buy/recipt.html", recipt=recipt)
                for m in error:
                    flash(m,'danger')
            if form["form_name"] == "plus":
                db.execute("UPDATE Cart SET Qty = Qty + 1 WHERE Client = ? AND PName = ?;",(g.user["Username"],form["item_name"],))
                db.commit()
            if form["form_name"] == "minus":
                db.execute("UPDATE Cart SET Qty = Qty - 1 WHERE Client = ? AND PName = ?;",(g.user["Username"],form["item_name"],))
                db.commit()
            if form["form_name"] == "delete":
                db.execute("DELETE FROM Cart WHERE Client = ? AND PName = ?;",(g.user["Username"],form["item_name"],))
                db.commit()
            return redirect(url_for("shop.cart"))
        except:
            error += ["An error ocurred! Cancelling process..."]
            for m in error:
                    flash(m,'danger')
            return redirect(url_for("shop.cart"))
    return render_template("buy/cart.html",cart=cart,title="Cart")

@bp.route("/profile",methods=("GET","POST"))
@login_required
def profile():
            
    db = get_db()
        
    # user = db.execute("SELECT Username,Name,PhoneNumber,Email,Age,Role FROM User Where ID = ?",(g.user["ID"],)).fetchone()
    # orders = db.execute("SELECT * FROM [Order] Where Client = ?",(user["Username"],)).fetchall()
    
    user = db.execute("SELECT Username,Name,PhoneNumber,Email,Age,Role FROM User Where Username = '"+g.user["Username"]+"'").fetchone()
    orders = db.execute("SELECT * FROM [Order] Where Client = '"+g.user["Username"]+"'").fetchall()
    
    a_orders = db.execute("SELECT op.Qty,Name,Price,[Order] FROM [Order] JOIN Order_Has_Product as op ON op.[Order]=ID JOIN Product ON PName=NAME Where Client = ?",(g.user["Username"],)).fetchall()
    
    if request.method == 'POST':
        sortt = request.form.get("sort")
        
        if sortt == "Date":
            orders.sort(key=lambda x:x["Date"])
            
        if sortt == "Price":
            orders.sort(key=lambda x: x["TotalPrice"])
    
    order_prods = dict()
    for o in orders:
        order_prods[o] = list( order for order in a_orders if order["Order"] == o["ID"]  )
                
    return render_template("user/profile.html",user=user,order_prods=order_prods,title="Profile")
