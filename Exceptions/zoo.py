from nameTooShortError import NameTooShortError
from dog1 import Dog
from owner import Owner

owner1 = Owner('Martina', 'London Road', '32172834568')

puppy1 = Dog('Betty', 'black', owner1)

puppy1.printOwnerDetails()

print(puppy1.name)

try:
    puppy1.name = 'abc'
except NameTooShortError as exc:
    print('Error occurred, name', exc.name, 'is too short.')

print(puppy1.name)


puppy2 = Dog('Buddy', 'brown', owner1)
print(puppy2.name)
try:
    puppy2.name = 'Ben'
except NameTooShortError as exc:
    print('Error occurred, name', exc.name, 'is too short.')
    print('Your dog has been renamed to Doggy')
    puppy2.name = 'Doggy'
except FileNotFoundError:
    print('File not found except')

print(puppy2.name)