import math

class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Method to calculate area. Must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area method.")

class Rectangle(Shape):
    """Class representing a rectangle, derived from Shape."""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle, derived from Shape."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * self.radius ** 2
