from Pet import Pet

name = input('Enter the name of your pet: ')
type_of_animal = input('Enter the type of your pet: ')
age = input('Enter the age of your pet: ')

pet = Pet(name, type_of_animal, age)

print(f"name: {pet.get_name()}, type of animal: {pet.get_animal_type()}, age of pet: {pet.get_age()}")
