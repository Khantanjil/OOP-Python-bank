# This is a class
class Account:

    # Constructor
    def __init__(self, filepath, name):
        self.filepath = filepath
        self.name = name
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    # Method to show the money
    def showQuantity(self):
        return f'{self.name}: {self.balance}'

    # Deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount

    # Withdraw method
    def withdraw(self, amount):
        self.balance = self.balance - amount

    # Method
    def __repr__(self):
        return f'The account user is: {self.name}\nThe file text is: {self.filepath}\nThe current balance: {self.balance}'

    # Save changes
    def commit(self):
        with open(self.filepath, 'r+') as file:
            file.write(str(self.balance))

# Object
john_account = Account("john_acc.txt", "john")
print(john_account.showQuantity())
john_account.withdraw(100)
print(john_account.showQuantity())
john_account.commit()

# Another Object
jack_account = Account("jack_acc.txt", "jack")
print(jack_account.showQuantity())
jack_account.deposit(200)
print(jack_account)
