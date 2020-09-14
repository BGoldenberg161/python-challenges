class BankAccount():
    def __init__(self, kind, pin):
        self.balance = 0
        self.overdraftFees = 0
        self.pin = pin
        self.kind = kind

    def withdraw(self, amount, pinFromUser):
        if(self.pin == pinFromUser):
            if(self.balance < amount):
                print('You broke son')
                return
            else:
                self.balance -= amount
            print(f'Your new balance is ${self.balance}.')
        else:
            print('PIN is incorrect')

        if(self.balance < 0):
            self.overdraftFees += 36

        print(f'Your new balance is ${self.balance}.')


    def deposit(self, amount, pinFromUser):
        if(self.pin == pinFromUser):
            self.balance += amount
            print(f'Your new balance is ${self.balance}.')
        else:
            print('PIN is incorrect')

    def change_pin(self, pin):
        self.pin = pin
        print(f'New PIN number is {self.pin}')


MyBank = BankAccount('savings', 1234)
MyBank.deposit(20000, 1234)
MyBank.withdraw(19500, 1244)
print('My overdraft fee is currently {}'.format(MyBank.overdraftFees))



