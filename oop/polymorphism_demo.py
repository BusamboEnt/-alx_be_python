# polymorphism_demo.py
import math

class Shape:
    """Base class for shapes. Subclasses should override area()."""

    def area(self):
        """Calculates the area of the shape. Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """Represents a rectangle."""

    def __init__(self, length, width):
        """Initializes a Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius):
        """Initializes a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return math.pi * self.radius**2