from Pet import Cat, Dog, Snake

pet_food = ["Red Meat", "Fish", "Egg", "Milk", "Chicken", "Banana"]

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        
    def walk(self):
        self.pet.play()
        print(f"{self.pet.name} moved")
        print(f'+{self.pet.health} Health Restored')
        return(self)
        
    def feed(self, food):
        self.pet.eat()
        print(f"{self.pet.name} ate {food}")
        print(f'+{self.pet.energy} Energy & +{self.pet.health} Health Restored')
        return(self)
        
    def bathe(self):
        self.pet.noise()
        print(f'{self.pet.name} is now Clean')
        return(self)
    
    def owner(self):
        print(f'{self.first_name}\'s pet')
        return(self)
    
    def display_stats(self):
        self.pet.show_HP_EP()
        return(self)