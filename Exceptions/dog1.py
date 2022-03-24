from nameTooShortError import NameTooShortError

class Dog:

    def __init__(self, name, colour, owner):
        self._name = name
        self._colour = colour
        #composition - 'has a'
        self._owner = owner

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 4:
            raise NameTooShortError(new_name)
        self._name = new_name

    def printOwnerDetails(self):
        if hasattr(self._owner, 'printDetails'):
            print(self._owner.printDetails())


