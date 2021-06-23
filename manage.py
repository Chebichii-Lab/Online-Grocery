from flask import Flask, render_template
# from forms import NameForm

from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Admin, Role
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
app = create_app('development')
# app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

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
    return dict(app=app, db=db, User=User, Admin=Admin, Role=Role)
    # pass

if __name__ == '__main__':
    manager.run()


 
