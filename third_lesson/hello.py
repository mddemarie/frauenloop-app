from flask import Flask, render_template
from forms import RestaurantForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a4267c9719bb78ad69dd1ab1305bd9b5'

restaurants = [
    {
        'id': 1,
        'name': '1990 Vegan living',
        'address': 'Krossener Str. 19, 10245 Berlin', 
        'food_type': 'vegan',
        'google_reviews': 4.6,
        'foodora_delivery': True
    },
    {
        'id': 2,
        'name': 'Chay Village',
        'address': 'Niederbarnimstraße 10, 10249 Berlin', 
        'food_type': 'vegetarian',
        'google_reviews': 4.5,
        'foodora_delivery': True
    },
    {
        'id': 3,
        'name': 'Gotcha',
        'address': 'Simon-Dach-Straße 6, 10245 Berlin', 
        'food_type': 'vietnamese',
        'google_reviews': 4.4,
        'foodora_delivery': True
    },
    {
        'id': 4,
        'name': 'Portofino',
        'address': 'Gubener Str. 48, 10243 Berlin', 
        'food_type': 'italian',
        'google_reviews': 4.6,
        'foodora_delivery': False
    },
    {
        'id': 5,
        'name': 'Speisehaus Berlin',
        'address': 'Wühlischstraße 30, 10245 Berlin', 
        'food_type': 'german',
        'google_reviews': 4.3,
        'foodora_delivery': False
    }
]

## How include works in Templates
# @app.route('/')
# def get_all_restaurants():
#     return render_template('index.html', restaurants=restaurants)

## TASK: USE BLOCK CONTENT FOR 1 RESTAURANT
# @app.route('/restaurant/1')
# def get_first_restaurant():
#     return render_template('index.html', restaurants=restaurants)

## Block content
@app.route('/restaurants')
def get_all_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)

# @app.route('/restaurant_form', methods=['GET', 'POST'])
# def get_restaurant_form():
#     form = RestaurantForm()
#     return render_template('register_restaurant.html', title='Register', form=form)