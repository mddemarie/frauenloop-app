from flask import jsonify

from project import app
from project.database import restaurants

@app.route('/restaurants', methods=['GET'])
def get_tasks():
    return jsonify({'restaurants': restaurants})