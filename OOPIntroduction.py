"""OOP allows programmers to create their own objects that have attributes and methods. These methods act as functions that use information about the object, as well as
the object itself to return results or change the current object.
OOP allows us to create code that is repeatable and organized"""


class NameOfClass:
    def __init__(self, param1, param2):  # allows u to create the instance.
        self.param1 = param1
        self.param2 = param2

    def some_method(self):  # through the self word we connect the methods to the class
        print(self.param1)
