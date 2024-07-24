# Define a class named Circle
class Circle :
    # class private variable pi and its value
    pi_circle = 3.141
    # Constructor method that initializes the Circle object with a list provided as an argument
    def __init__(self,radius):
        # Initialize the instance variable 'radius' with the radius
        self.radius = radius
    # Method named 'area' that returns the instance variable 'radius'
    def area(self):
        return self.radii
# Create an instance of the Circle class with the instance variable value of radius as 5   
a = Circle(5)
# Call the 'area' method on the instance 'a' and print the returned radius
print("radii :",a.area())
# Call and print the pi value with the instance 'a'
print("pi value :",a.pi_circle)
