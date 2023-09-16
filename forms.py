from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, IntegerField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, NumberRange

flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Ube', 'Pandan', 'Fig', 'Black Sesame', 'Rosemary', 'Brown Butter', 'Espresso', 'Red Velvet', 
'Hummingbird', 'Matcha', 'Lemon', 'Lime', 'Orange', 'Yuzu', 'Lavender', 'Earl Grey', 'Coconut', 'Carrot', 'Golden Milk', 'Mixed Berry', 'Tamarind', 
'Banana', 'Mountain Dew', 'Corn', 'Honey', 'Chai', 'Peach', 'Lychee']

flavor_choices = [(flavor, flavor) for flavor in flavors]


class CakeForm(FlaskForm):

    trust = BooleanField('Trust')
    size = SelectField('Size', choices=[( 6, '6in (serves 8-10)'), (8, '8in (serves 12-15)'), (10, '10in (serves 20-25)')])
    layers = SelectField('Layers', choices=[1,2,3])
    flavor = SelectField('Flavor', choices=flavors)
    frosting = SelectField('Frosting', choices=[('vaniller', 'vanilla'), ('buttcream', 'buttcream')])
    filling = SelectField('Filling', choices=[('jam', 'jam'), ('jelly', 'jelly')])
    colors = TextAreaField('Preferred Colors')
    occasion = TextAreaField('Occasion (optional)')
    date = DateField('Date')


"""

Chocolate, Vanilla, Strawberry, Ube, Pandan, Fig, Black Sesame, Rosemary, Brown Butter, Espresso, Red Velvet, 
Hummingbird, Matcha, Lemon, Lime, Orange, Yuzu, Lavender, Earl Grey, Coconut, Carrot, Golden Milk, Mixed Berry, Tamarind, 
Banana, Mountain Dew, Corn, Honey, Chai, Peach, Lychee

Swiss Meringue Buttercream, American Buttercream, Cream Cheese

Jam, compote, cream cheese, caramel: $5+
Curd, ganache, caramelized honey, pastry cream: $10+

Simple piped lambeth
Funky naked
Swirl base: $5+
Chaos cake: +$20
Heavily piped lambeth: +30%
Florals: MKTP
Glitter cherries: +$5
Keepsake bows: +$5
Disco balls: +$10
Dried flowers: +$10
Star, heart, butterfly, coffin: +$10
Egg: +$20
Tree Trunk: +$20
Writing: $5+ """