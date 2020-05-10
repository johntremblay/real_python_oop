"""
A class that will take another class
"""

class Material:
    def __init__(self, type_of_material: str, resistance: int):
        self.type_of_material = type_of_material
        self.resistance = resistance

    def description(self):
        return f'This is {self.type_of_material} and has a duration of {self.resistance}'

    def add_resistance(self):
        self.resistance += 1


class Door:

    def __init__(self, material: Material, color: str, location: str):
        self.material = material
        self.color = color
        self.location = location

    def add_coating(self, add_resist):
        self.material.resistance = self.material.resistance + add_resist

    def __str__(self):
        return f'a {self.color} {self.__class__} with resist {self.material.resistance}'


# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”.
if __name__ == "__main__":
    door_mat = Material('hard wood', 12)
    main_door = Door(door_mat, 'black', 'entrance')
    print(main_door.material.resistance)
    main_door.add_coating(20)
    print(main_door.material.resistance)
    print(repr(main_door))



else:
    print('Executed when imported')
