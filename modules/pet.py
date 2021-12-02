class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks, energy = 100, health = 100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health

    def show_stats(self):
        print(f'Name: {self.name}\nType: {self.type}\nTricks: {self.tricks}\nEnergy: {self.energy}\nHealth: {self.health}\n')
        return self
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.health += 10
        self.energy += 5
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        self.show_stats()
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print("meow")
        return self
