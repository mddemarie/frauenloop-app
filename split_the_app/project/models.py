from project import db

# restaurants = [
#     {
#         'id': 1,
#         'restaurant': '1990 Vegan living',
#         'address': 'Krossener Str. 19, 10245 Berlin', 
#         'food_type': 'vegan',
#         'google_reviews': 4.6,
#         'foodora_delivery': True
#     }
# ]

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(30), unique=True, nullable=False)
    food_type = db.Column(db.String(5), unique=True, nullable=False)
    google_reviews = db.Column(db.Float)
    foodora_delivery = db.Column(db.Boolean)