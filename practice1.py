

#parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}\nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg
    
#child class instance
class Human(Organism):
    name = "John"
    species = "Homosapian"
    legs = 2
    arms = 2
    origin = "Earth"

    def personality(self):
        msg = "\n Is super boring but you know hes a good guy"
        return msg

#another child class instance
class Dog(Organism):
    name = "Kiwi"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg ="\nEmits a loud, menacing growl and bites down ferociuosly on its target"

#another child class isntance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cells divide and multiply"
        return msg


if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.personality())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
