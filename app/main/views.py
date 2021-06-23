from flask.helpers import flash
from . import main
from flask import render_template
from ..models import ProductItem,CartItem
from .. import db




@main.route('/')
def order():
   
    cart = ProductItem.query.all()
    return render_template("product.html",title='Order and delivery',cart=cart)

@main.route('/cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):

    product = ProductItem.query.filter(ProductItem.id == product_id)
    cart_item = CartItem(product=product)
    db.session.add(cart_item)
    db.session.commit()

    return render_template('order.html', product=product,cart_item=cart_item)

