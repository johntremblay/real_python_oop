"""
Basic class definition
"""

class Dog:
    # this is a class attribute, it is not independent from a instance of a class to another
    _species = 'mammal'

    def __init__(self, name: str, age: int):
        # the below are instance attributes and will be independent from an instance to another
        self.age = age
        self.name = name

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, things_to_say: str):
        return f'{self.name} says {things_to_say}'


# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”.
if __name__ == "__main__":
    a = Dog(name='ti chum', age=3)
    b = Dog(name='corneille', age=1)

    print(a.speak('chu gay'))


else:
    print('Executed when imported')
