from flask.helpers import flash
from . import main
from flask import render_template

@main.route('/')
def index():
    return render_template('form.html')

# #@main.route('/')
# def order():
   
#     return render_template("order.html",title='Order and delivery')

# @main.route('/')
# def addtocart():
#     flash("added to the cart")
   
#     return render_template("order.html",title='Order and delivery')

