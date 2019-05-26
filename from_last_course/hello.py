from flask import Flask, render_template

app = Flask(__name__)

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

## Controller
@app.route('/restaurants')
def get_all_restaurants():
    return render_template('restaurants.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug = True)