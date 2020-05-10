"""
A class that will consider shapes classes
"""

class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width


class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        super().__init__(base=base, **kwargs)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


class Cube(Square, SurfaceAreaMixin):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [Square, Square, Square, Square, Square, Square]

# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value “__main__”.
if __name__ == "__main__":
    cube = Cube(3)
    print(cube.surface_area())

else:
    print('Executed when imported')
