from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, NumberRange

class CakeForm(FlaskForm):

    trust = BooleanField('Trust')
    size = SelectField('Size', choices=[( 6, '6in (serves 8-10)'), (8, '8in (serves 12-15)'), (10, '10in (serves 20-25)')])
    flavor = SelectField('Flavor', choices=[('chocolate', 'chocolate'), ('earl grey', 'earl grey')])
    frosting = SelectField('Frosting', choices=[('vaniller', 'vanilla'), ('buttcream', 'buttcream')])
    filling = SelectField('Filling', choices=[('jam', 'jam'), ('jelly', 'jelly')])
    colors = TextAreaField('Preferred Colors')
    occasion = TextAreaField('Occasion (optional)')
    date = DateField('Date')