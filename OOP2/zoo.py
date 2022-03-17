from nameTooShortError import NameTooShortError
from dog1 import Dog

puppy1 = Dog('Betty', 'black')
print(puppy1.name)
try:
    puppy1.name = 'abc'
except NameTooShortError as exc:
    print('Error occurred, name', exc.name, 'is too short.')

print(puppy1.name)


puppy2 = Dog('Buddy', 'brown')
print(puppy2.name)
try:
    puppy2.name = 'Ben'
except NameTooShortError as exc:
    print('Error occurred, name', exc.name, 'is too short.')
    print('Your dog has been renamed to Doggy')
    puppy2.name = 'Doggy'

print(puppy2.name)