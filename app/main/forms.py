from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField 
from wtforms.validators import DataRequired, Email
 

class NameForm(FlaskForm):
    username = StringField('Destination to be delivered',)
    email = StringField('email', validators=[DataRequired(), Email()])
    place = StringField('Delivery fee is ksh.100')
    send = SubmitField('Submit')