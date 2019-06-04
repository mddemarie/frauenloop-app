from flask import request

from project.models import User
from project import app

@app.route('/')
def home_page():
    return 'This is a Bank Account App!!!'

# http://127.0.0.1:5000/balance?pin=1234&user=user2
@app.route('/balance')
def display_balance():
    pin_number = request.args.get('pin') #
    user_name = request.args.get('user') #
    if pin_number == users[user_name][0]:
        return 'This is your current balance: {} EUR'.format(users[user_name][1])
    else:
        return pin_error()

def pin_error():
    return 'Access denied: incorrect PIN.'

# http://127.0.0.1:5000/withdraw?pin=1234&user=user1&amount=50
@app.route('/withdraw')
def withdraw_money():
    pin_number = request.args.get('pin') #
    user_name = request.args.get('user') #
    amount = request.args.get('amount') #
    amount = int(amount) # why does this have to be transformed into integer?

    balance = users[user_name][1]
    if pin_number == users[user_name][0]:
        if amount <= balance:
            balance = balance - amount
            return 'Withdrew {} EUR. New balance is: {} EUR.'.format(amount, balance)
        else:
            return 'You are not allowed to withdraw more money than you have on your account!'
    else:
        return pin_error()