balance = 100
list_with_pins = {'user1': 1234, 'user2': 5576, 'user3': 2293}

def display_balance(pin_number, user):
    if pin_number == list_with_pins[user]:
        return 'This is your current balance: {} EUR'.format(balance)
    else:
        pin_error()

def pin_error():
    return 'Access denied: incorrect PIN.'

print(display_balance(1234, 'user1'))

## Write a similar function called 'withdraw_money'
## withdraw_money should have 2 args 'pin_number' and 'amount'
## 1. check if pin is correct, if not return the error
## 2. check if amount is smaller or equal to balance, if so: substract the amount and return e.g. 'Withdrew 30 EUR. New balance is: 2000 EUR.
## otherwise return 'You are not allowed to withdraw more money than you have on your account!'

## Write a function called 'transfer_money'