from dog import Dog

puppy = Dog("Missy")
puppy.run()
print(puppy.name)


puppy2 = Dog('Buddy')
puppy2.run()

puppy3 = Dog('Betty')
puppy3.run()
puppy3.fetch('slipper')
puppy2.fetch('newspapers')
puppy.fetch('stick')