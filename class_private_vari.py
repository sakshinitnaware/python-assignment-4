# Define a class named Circle
class Circle :
    # class private variable pi and its value
    __pi_circle = 3.141
    # Constructor method that initializes the Circle object with a list provided as an argument
    def __init__(self,radius):
        # Initialize the instance variable 'radius' with the radius
        self.radius = radius
    # Method named 'area' that returns the area accessing the private variable pi'
    def area(self):
        area = self.__pi_circle * self.radius**2 
        return area
# Create an instance of the Circle class with the instance variable value of radius as 5   
a = Circle(5)
# Call the 'area' method on the instance 'a' and print the returned radius
print("radius :",a.area())
