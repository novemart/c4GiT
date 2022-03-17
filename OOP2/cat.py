from pet import Pet


class Cat(Pet):

    # class attribute
    owner = 'Martina'

    # constructor
    def __init__(self, name, colour, age):
        # _name is an instance attribute
        super().__init__(name, colour)
        self._age = age

    def print_name(self):
        super().print_name()
        print('My colour is', self._colour)

    def speak(self):
        print('Meow meow')

    def rename(self, new_name):
        self._name = new_name
        self._change_colour('purple')

    def _change_colour(self, newColour):
        self._colour = newColour

    @classmethod
    def say_hello(cls):
        print('Hello')

    def __str__(self):
        return "Meow, I'm a cat and my name is " + self._name

    def __bool__(self):
        if self._colour == 'white':
            return True
        else:
            return False

    def __len__(self):
        return len(self._name)

    #getter method
    def get_age(self):
        return self._age

    #setter method
    def set_name(self, new_name):
        if len(new_name) > 5:
            self._name = new_name

    def move(self):
        print('Im lazy and hardly move')
