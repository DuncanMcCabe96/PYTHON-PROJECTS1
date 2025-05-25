from abc import ABC, abstractmethod

class Animal(ABC):
    #abstract method - must be implemented by subclasses
    def make_sound(self):
        pass
    #Regular method - can be inheretied or overidden
    def sleep(self):
        print("The animal is sleeping")

class Dog(Animal):
    #implementation of the abstract method
    def make_sound(self):
        print("Dog barks: Woof Woof!")

#Create an object of dog
my_dog_obj = Dog()
#call the implemented abstract method
my_dog_obj.make_sound()
#Call the regular method inherited from Animal
my_dog_obj.sleep()
