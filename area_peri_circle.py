# Import the math module to access mathematical functions like pi
import math 
# Define a class named Circle
class Circle :
    # Constructor method that initializes an instance of Circle with a radius
    def __init__(self,radius):
         # Initialize the instance variable 'radius' with the value passed as 'radius'
        self.radius = radius
    # Method to calculate and return the area of the circle   
    def area(self):
        area = math.pi * self.radius**2  # Area = π * r^2
        return area     # Return the calculated area
    # Method to calculate and return the perimeter of the circle
    def perimeter(self):
        peri = 2 * math.pi * self.radius  # Circumference = 2 * π * r
        return peri      # Return the calculated perimeter

# Create an instance of the Circle class with radius 5   
a = Circle(5)
# Print the radius of the circle, accessed using the instance variable 'radius'
print("radius of circle :",a.radius)
# Print the area of the circle using the area() method
print(f"area : {a.area()} cmsq")
# Print the area of the circle using the perimeter() method
print(f"peri : {a.perimeter()} cm")
