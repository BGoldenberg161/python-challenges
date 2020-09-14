print("Welcome to Chase bank.")
print("Have a nice day!")

balance = 0

def bank():
    action = input('What would you like to do? (deposit, withdraw, check_balance)\n')
    if action == 'deposit':
        amount = input('How much would you like to deposit?\n')
        balance = int(balance) + int(amount)
        print(f'Your current balance is {balance}.')
        action = input('Are you done? (yes, no)\n')
        if action == 'yes':
            return
        elif action == 'no':
            bank()
    if action == 'withdraw':
        amount = input('How much would you like to withdraw?\n')
        balance = int(balance) + int(amount)
        print(f'Your current balance is {balance}.')
        action = input('Are you done? (yes, no)\n')
        if action == 'yes':
            return
        elif action == 'no':
            bank()
    if action == 'check_balance':
        print(f'Your current balance is {balance}.')
        action = input('Are you done? (yes, no)\n')
        if action == 'yes':
            return
        elif action == 'no':
            bank()
print(bank())

