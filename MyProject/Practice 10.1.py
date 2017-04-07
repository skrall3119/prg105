class Personal:

    # constructor
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone

    # getters
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

    # setters
    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone(self, phone):
        self.__phone = phone

    def __str__(self):
        person = self.get_name() + ' is ' + self.get_age() + " Years Old, lives on " + self.get_address() + ' and their phone number is ' + self.get_phone()
        return person


person_1 = Personal('Soz-Oz Kaboz', '1234 Street St.', '16', '18472748866')
person_2 = Personal('Dalton the Rat', '889 Happy Blvd', '72', '2249429957')
person_3 = Personal('Kid Bruv', '7623 Intermediate ave.', '999999999', '16302496452')


print(person_1)
print(person_2)
print(person_3)
