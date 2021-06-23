from flask_wtf import FlaskForm
from wtforms import  StringField,SubmitField 
 
class NameForm(FlaskForm):
    name = StringField('Destination to be delivered',)
    place = StringField('Delivery fee is ksh.100')
    submit = SubmitField('Submit')