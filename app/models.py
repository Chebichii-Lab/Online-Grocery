from . import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    pass_secure = db.Column(db.String(255))
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

        
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class ProductItem(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    descr = db.Column(db.Text,unique=True,nullable=True)
    price = db.Column(db.Float,nullable=False)
    img = db.Column(db.String(64),unique=True)
    # cartitems = db.relationship('CartItem', backref='Product')
    def __repr__(self):
        return f"ProductItem('{self.name}', '{self.price}','{self.img}')"

# class CartItem(db.Model):
#     __tablename__='cartitems'
#     id = db.Column(db.Integer,primary_key=True)
#     # adding the foreign key
#     product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    
    