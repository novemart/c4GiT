class Pet:

    def __init__(self, name, colour):
        self._name = name
        self._colour = colour

    def eat(self):
        print(self._name, 'is eating')

    def sleep(self):
        print(self._name, 'is sleeping')

    def print_name(self):
        print('Hi, my name is ', self._name)

    def move(self):
        print('move')