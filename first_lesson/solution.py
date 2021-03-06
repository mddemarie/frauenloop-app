from flask import Flask, jsonify

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

@app.route('/restaurants')
def get_restaurants():
    return jsonify(restaurants)

# SOLUTION of the task:
@app.route('/restaurant/1')
def get_one_restaurant():
    return jsonify(restaurants[0])

# OR:
# @app.route('/restaurant/<int:restaurant_id>')
# def get_any_restaurant(restaurant_id):
#     for rest_num in range(len(restaurants) + 1):
#         if restaurants[rest_num]['id'] == restaurant_id:
#             return jsonify(restaurants[restaurant_id])

if __name__ == '__main__':
    app.run(debug = True)
