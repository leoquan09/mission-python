class Pet: 
    def __init__(self, name, type_of_pet, age):
        self.name = name
        self.animal_type = type_of_pet
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_animal_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age
