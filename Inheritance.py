class Animal():
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i (self):
        print("I am an animal.")

    def eat (self):
        print("I am eating!")


my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()


class Dog(Animal):  # lets inherit from the base class
    def __init__(self):
        Animal.__init__(self)
        print("Dog created.")

    # lets use some methods from the base class
    def who_am_i(self):  # lets override this method
        print("I am a dog")

    def bark(self):
        print("Woof!")


my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()


# Polymorphism in Python refers to the way in which different object classes can share the same method name.
# And then those methods can be called from the same place even though a variety of different objects

class Snake():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says ssss"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


niko = Snake("niko")
felix = Cat("felix")
print(niko.speak())
print(felix.speak())

# notice how both classes have a speak method, but when called they both give a unique result. This is polymorphism.
# we can demonstrate polymorphism like this too:

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))


# Or through a function
def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)


# Abstract classes never expect to be initiated. Its just designed to basically serve as a base class.

class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Snake(Animal):
    def speak(self):
        return self.name + " says sss"


class Cat(Animal):
    def speak(self):
        return self.name + " says meow"


fidel = Snake("fidel")
isis = Cat("isis")
print(fidel.speak())
print(isis.speak())
