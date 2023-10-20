import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from Database.db import get_db

bp = Blueprint('productDetails', __name__, url_prefix='/productDetails')

@bp.before_request
@bp.route('/', methods=('GET', 'POST'))
def product():
    if request.method == 'GET':
        name=request.args.get("name")
        db=get_db()
        
        try:
            query=db.execute( "SELECT * FROM Product WHERE Name=?",(name,))
            query=query.fetchall()
            if len(query)==0:
                return
            db.commit()
        except db.IntegrityError:
            error += [f"Product {name} does not exist."]
    else:
        flash("Item successfully added to the Cart!","info")
        
    return render_template('product/productDetails.html',size=True,color=True,name=query[0][0],description=query[0][1],price=query[0][3],image="https://img.freepik.com/fotos-premium/o-suricato-suricata-suricatta-ou-suricate-e-um-pequeno-mangusto-encontrado-no-sul-da-africa_208861-941.jpg")