from cat import Cat
from dog import Dog

print(Cat.owner)
kitty = Cat('Luna', 'white', 4)

kitty.print_name()

kitty.print_name()

Cat.say_hello()

print(kitty)

if kitty:
    print("kitty is True")

print(len(kitty))

print(kitty.get_age())

kitty.set_name('Agnes1')
kitty.print_name()

kitty.eat()

doggy = Dog('Betty', 'black', 10)
doggy.print_name()

doggy.move()