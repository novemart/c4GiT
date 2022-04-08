class Owner:

    def __init__(self, fname, lname, address):
        self._fname = fname
        self._lname = lname
        self._address = address

    def __str__(self):
        return "Hi, my name is "+ self._fname + " " + self._lname