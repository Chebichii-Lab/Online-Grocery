from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Email,EqualTo

class NameForm(FlaskForm):
    name = StringField('Destination to be delivered', validators=[DataRequired()])
    submit = SubmitField('Submit')