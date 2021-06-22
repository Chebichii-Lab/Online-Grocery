from . import main
from flask import render_template



@main.route('')
def order():
   
    return render_template("order.html",title='Order and delivery')
