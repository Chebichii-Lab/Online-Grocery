from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = "DELIVERY FORM"
    return render_template("index.html", title=title)

@app.route('/about')
def about():
    title = ""