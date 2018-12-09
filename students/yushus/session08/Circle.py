

from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__diameter = 2*self.__radius

    @property
    def radius(self):
        return self.__radius

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter 
    def diameter(self, value):
        if value < 0:
            raise ValueError('Diameter cannot be < 0')
        self.__diameter = value
        self.__radius = self.__diameter / 2

    @property
    def area(self):
        return pi * self.__radius * self.__radius

    @classmethod
    def from_diameter(class_object, value):
        print(class_object)
        return class_object(value/2)

    def __str__(self):
        return f'Circle with radius: {self.__radius:.6f}'

    def __repr__(self):
        return f'Circle({self.__radius})'
    
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError('{other} has to be a Circle type')

    def __mul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        raise TypeError('{other} has to be an int type')

    def __rmul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        raise TypeError('{other} has to be an int type')
    
    def __iadd__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise TypeError('{other} has to be a Circle type')

    def __imul__(self, other):
        if isinstance(other, int):
            return Circle(self.radius * other)
        raise TypeError('{other} has to be an int type')

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        raise TypeError('{other} has to be a Circle type')

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.radius <= other.radius
        raise TypeError('{other} has to be a Circle type')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        raise TypeError('{other} has to be a Circle type')

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __sort__(self, circles):
        return sorted(circles, key=lambda circle: circle.radius, reverse=True) 
        #return circles.sort(key=lambda c: c.radius, reverse=True)

class Sphere(Circle):

    # def __init__(self, radius):
    #     self.__radius = radius
    #     super().__init__(radius)

    @property
    def area(self):
        return pi * super().radius * super().radius * 4

    @property
    def volume(self):
        return pi * super().radius * super().radius* super().radius * 4 / 3
    
    def __str__(self):
        return f'Sphere with radius: {super().radius:.6f}'

    def __repr__(self):
        return f'Sphere({super().radius})'