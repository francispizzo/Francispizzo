# pet = {
#     "name": "Doggo",
#     "animal": "dog",
#     "species": "labrador",
#     "age": 5
# }

class Pet(object):
    def __init__(self, name, age, animal, location):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = "happy"
        self.location = "room 1"
    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> may have eaten too much." % self.name)
            self.mood = "lethargic"
    def move(self):
            print("> %s is moving..." % self.name)
        if self.location == "room 1"
           self.location = "room 2"
           print("> %s is in %s" % (self.name, self.location))
       else:
           self.location = "room 2"
           print("> %s is in %s" % (self.name, self.location))
# my_pet = Pet("Fido", 3)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Bill", 1)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Peanut", 4)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))
# my_pet = Pet("Gabe", 2)
# print("My pet %s is %s years old" % (my_pet.name, my_pet.age))



my_pet = Pet("Fido", 3, "dog")

my_pet.is_hungry = True
print("Is my pet hungry? %s" % my_pet.is_hungry)
my_pet.eat()
print("How about now? %s" % my_pet.is_hungry)
print("My pet is feeling %s" % my_pet.mood)
