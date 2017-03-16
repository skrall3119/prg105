class Dog(object):

    # Class Object Attribute
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = "Black Lab"
        self.name = name
murray = Dog(breed= "Black Lab", name="Murray")
print(murray.breed)
print(murray.name)
