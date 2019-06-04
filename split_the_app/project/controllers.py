from flask import jsonify

from project import app
from project.database import restaurants

@app.route('/restaurants')
def get_restaurants():
    return jsonify({'restaurants': restaurants})