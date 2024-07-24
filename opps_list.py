# Define a class named Circle
class Circle:
    # Constructor method that initializes the Circle object with a list provided as an argument
    def __init__(self, my_list):
        # Initialize the instance variable 'list' with the value of 'my_list'
        self.list = my_list
    # Method named 'task_list' that modifies the instance variable 'list'
    def task_list(self) :
        # Set the instance variable 'list' to [1, 2, 3, 4]
        self.list = [1,2,3,4]
        # Return the updated list
        return self.list

# Create an instance of the Circle class with an empty list as the initial value
r = Circle([])
# Call the 'task_list' method on the instance 'r' and print the returned list
print(r.task_list())
