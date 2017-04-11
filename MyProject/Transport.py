# define a parent class
class Transport:
    # class attributes
    MODES = {1: 'land', 2: 'sea', 3: 'air'}
    CARGO_TYPE = {1: 'freight', 2: 'people'}

    # constructor
    def __init__(self, mode = None, cargo = None):
        self.__mode = None
        self.set_mode(mode)
        self.__cargo = None
        self.set_cargo(cargo)

    # setters
    def set_mode(self, mode):
        if mode in Transport.MODES:
            self.__mode = mode
        else:
            self.__mode = None

    def set_cargo(self, cargo):
        if cargo in Transport.CARGO_TYPE:
            self.__cargo = cargo
        else:
            self.__cargo = None

    # getters
    def get_mode(self):
        return self.__mode

    def get_cargo(self):
        return self.__cargo

    # string representation of the object
    def __str__(self):
        return "This is a " + Transport.MODES[self.__mode] + " vehicle that transports " + \
               Transport.CARGO_TYPE[self.__cargo] + "."


# the class Car is a child of the class Transport
# it inherits all attributes and methods from its parent
class Car(Transport):
    # constructor
    def __init__(self, make=None, model=None, year=None, color=None):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__color = color
        Transport.__init__(self, 1, 2)      # call parent class __init__

    # setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    # getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    # string representation
    def __str__(self):
        result = Transport.__str__(self)
        if self.__make is None and self.__model is None and self.__year is None and self.__color is None:
            return result + " Details for this vehicle are unknown."
        else:
            result += " It is a"
            # add all known details
            if self.__color is not None:
                result += ' ' + self.__color
            if self.__year is not None:
                result += ' ' + self.__year
            if self.__make is not None:
                result += ' ' + self.__make
            if self.__model is not None:
                result += ' ' + self.__model
            return result + "."
generic = Transport(2, 2)
print(generic)
generic.set_cargo(1)
print(generic)

my_car = Car('Ford', 'Mustang', '1980', 'Blue')
print(my_car)
van = Car('Chrysler', 'Town and Country', '1992', 'forest green')
van.set_year('1996')
van.set_color('electric blue')
print(van)
