class Pet:
    
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 10
        self.health = 10
        
    def sleep(self):
        self.energy +=25
        return(self)
            
    def eat(self):
        self.energy +=5
        self.health +=10
        return(self)
        
    def play(self):
        self.health +=5
        return(self)
        
    def noise(self):
        print(f'{self.name} took a Bath')
        if self.type == "Cat":
            print("Meow")
        elif self.type == "Dog":
            print("Woof")
        elif self.type == "Snake":
            print("Hiss")
    
    def show_HP_EP(self):
        print(f'{self.name}\'s Status:')
        print(f'HP:{self.health} EP:{self.energy}')
        
class Cat(Pet):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 6
        self.health = 8
        
    def sleep(self):
        self.energy +=28
        return(self)
            
    def eat(self):
        self.energy +=5
        self.health +=2
        return(self)
        
    def play(self):
        self.health +=12
        return(self)
        
    def noise(self):
        print(f'{self.name} took a Bath')
        print("Meow")

class Dog(Pet):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 18
        self.health = 15
        
    def sleep(self):
        self.energy +=38
        return(self)
            
    def eat(self):
        self.energy +=7
        self.health +=11
        return(self)
        
    def play(self):
        self.health +=3
        return(self)
        
    def noise(self):
        print(f'{self.name} took a Bath')
        print("Woof")

class Snake(Pet):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 2
        self.health = 4
        
    def sleep(self):
        self.energy +=30
        return(self)
            
    def eat(self):
        self.energy +=8
        self.health +=10
        return(self)
        
    def play(self):
        self.health +=2
        return(self)
        
    def noise(self):
        print(f'{self.name} took a Bath')
        print("Hiss")
