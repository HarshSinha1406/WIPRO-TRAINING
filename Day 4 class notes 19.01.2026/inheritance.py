class Animal:
    def speaks(self):
        print("I'm an animal who speaks")

class Dog(Animal):
    def bark(self):
        print("I'm a dog who bark")

d = Dog()
d.speaks()
d.bark()