from Pet import Cat, Dog, Snake
from Ninja import Ninja

pet_food = ["Red Meat", "Fish", "Egg", "Milk", "Chicken", "Banana"]

pet01 = Cat("Pucchi", "Cat", 3)
pet02 = Dog("Rex", "Dog", 5)
pet03 = Snake("Asmodeus", "Snake", 1)

ninja01 = Ninja("Nelo", "Angelo", "Fish-chunks", pet_food[2], pet01)
ninja02 = Ninja("Lara", "Croft", "Milk-bones", pet_food[2], pet02)
ninja03 = Ninja("Claire", "Redfield", "Meat-shanks", pet_food[2], pet03)

ninja01.owner().feed(pet_food[1]).walk().bathe()
print()
ninja02.owner().feed(pet_food[0]).walk().bathe()
print()
ninja03.owner().feed(pet_food[0]).walk().bathe()
