class NameTooShortError(Exception):
    def __init__(self, name):
        super().__init__(self)
        self._name = name

    @property
    def name(self):
        return self._name