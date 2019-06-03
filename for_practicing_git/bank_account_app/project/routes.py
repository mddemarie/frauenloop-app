from flask import request

from project import app
from project.database import users

@app.route('/balance')
def display_balance():
    pin_number = request.args.get('pin')
    user = request.args.get('user')
    if pin_number == users[user][0]:
        return 'This is your current balance: {} EUR'.format(users[user][1])
    else:
        return pin_error()

def pin_error():
    return 'Access denied: incorrect PIN.'

@app.route('/withdraw')
def withdraw_money():
    pin_number = request.args.get('pin')
    user_name = request.args.get('user')
    amount = request.args.get('amount')
    amount = int(amount)

    balance = users[user_name][1]
    if pin_number == users[user_name][0]:
        if amount <= balance:
            balance = balance - amount
            return 'Withdrew {} EUR. New balance is: {} EUR.'.format(amount, balance)
        else:
            return 'You are not allowed to withdraw more money than you have on your account!'
    else:
        return pin_error()