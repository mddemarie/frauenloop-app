from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

# @app.route('/notify')
# def notify_me():
#     return 'Notification fired!'
