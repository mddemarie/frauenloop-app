from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RestaurantForm(FlaskForm):
    restaurant_name = StringField('Username')
    # email = StringField('Email')
    # password = PasswordField('Password')
    submit = SubmitField('Add restaurant')

