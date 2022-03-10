class Dog:

    name=''

    #constructor
    def __init__(self, str):
        self.name = str

    def run(self):
        print("Im runninnnnnnnng and my name is", self.name)

    def fetch(self, thing):
        print(self.name, "Im fetching a", thing)