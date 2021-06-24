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

 
from flask.cli import with_appcontext
# Creating app instance.
app = create_app("development")
manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Admin=Admin, Role=Role)
    # pass

if __name__ == '__main__':
    app.run()
    

 

 
