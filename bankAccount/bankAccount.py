class BankAccount:

    def __init__(self, owner, init_balance):
        # composition
        self._owner = owner
        self._balance = init_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount

    def __str__(self):
        return str(self._owner) + " and I have " + str(self._balance) +" pounds"