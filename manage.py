from flask import Flask, render_template
from forms import NameForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 38977877

app.route('/')
def home():
    return 'DELIVERY'
   
app.route('/form')
def form():
    
    return  render_template('form.html')

app.route('/DeliveryForm')
def delivery():
    return render_template('form.html', form=form)
    
 
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)
    # pass

if __name__ == '__main__':
    manager.run()


 
