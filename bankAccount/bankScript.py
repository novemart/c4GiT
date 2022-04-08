from bankAccount import BankAccount
from owner import Owner

owner = Owner('John', 'Doe', 'London Road, Leeds')
my_acc = BankAccount(owner, 0)
my_acc.deposit(500)
print(my_acc)

my_acc.withdraw(300)
print(my_acc)