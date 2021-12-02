from modules.pet import Pet
class Ninja:

# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, pet, treats = 3):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet = pet
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
