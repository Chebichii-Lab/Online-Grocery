from app import request
from flask import Flask, render_template
 

app = Flask(__name__)
app.config['SECRET_KEY'] = "38977877"

app.route('/')
def home():
    return 'DELIVERY'
   
app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
     username = request.form["username"]
     email = request.form["email"]
     place = request.form["place"]
     return username + email + "Your oder will be delivered to" + place
    return  render_template('form.html')

app.route('/DeliveryForm')
def delivery():
    return render_template('form.html', form=form)
    

if __name__ == '__main__':
    app.run()


 
