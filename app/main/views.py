from flask.helpers import flash
from . import main
from flask import render_template
from ..models import ProductItem



@main.route('/')
def order():
    products = ProductItem.query.all()
    return render_template("order.html",title='Order and delivery',products=products)

@main.route('/')
def addtocart():
    flash("added to the cart")
   
    return render_template("order.html",title='Order and delivery')

