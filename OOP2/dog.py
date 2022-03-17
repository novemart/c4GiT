from pet import Pet

# inheritance
class Dog(Pet):

    def __init__(self, name, colour, speed):
        #calling parent's constructor
        super().__init__(name, colour)
        self._speed = speed

    def run(self):
        print('woof woof', 'Im running', self._name)

    def print_name(self):
        super().print_name()
        print('Woof woof')

    def move(self):
        print('Run')