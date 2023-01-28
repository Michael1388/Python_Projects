# Python 3.10.9
#
# Michael LaRocca
# 
# Steps 239, 241 OOP and Classes Video part one and two exercises
# Follow along

"""
class Game:
    var1 = 'Hello'
    var2 = 'World!'


if __name__ == "__main__": #control the program flow
    x = Game() 
    print(x.var1)
    print("{} {}".format(x.var1,x.var2))

"""

# parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self): #classes of "self"
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\
            \nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format\
            (self.name,self.species,self.legs,self.arms,self.dna,self.origin,\
            self.carbon_based)
        return msg

# child class instance 1
class Human(Organism):
    name = "McDonald"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth" 

    # give it a method
    def ingenuity(self):
        msg = "\nCreates a hamburger with thousand island dressing, calls it a BigMac \nand people eat it!"
        return msg

# child class instance 2
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    # give it a method
    def bite(self):
        msg = "\nEmits a loud, annoying yip yip noise, bites down on it's target!"
        return msg
   
#child class instance 3
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

# give it a method
    def replication(self):
        msg = "\nCells divide and multiply into two separate organisms!"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.ingenuity())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria=Bacterium()
    print(bacteria.information())
    print(bacteria.replication())




   