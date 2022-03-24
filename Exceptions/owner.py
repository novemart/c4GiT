class Owner:

    def __init__(self, first_name, address, phoneNumber):
        self._first_name = first_name
        self._address = address
        self._phoneNumber = phoneNumber

    def printDetails(self):
        print(self._first_name, self._phoneNumber)
