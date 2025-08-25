#A program with private attribute (__value) and get methods (getValue) and set methods (setValue) for the die value.
class die:
    def __init__(self):
        self.__value = 1        # Private attribute to store the die value

    @property       # Property decorator to create a getter for the private attribute
    def Value(self):         # Get method to access private attribute(getValue)
        return self.__value
    
    @Value.setter  # Setter decorator to create a setter for the private attribute
    def Value(self, value):  # Set method to modify private attribute(setValue)
        if 1 <= value <= 6:
            raise ValueError("Value must be between 1 and 6") # Raise an error if value is out of range
        else:
            self.__value = value
    
    def roll(self): # Roll the die to get a random value between 1 and 6
        import random
        self.__value = random.randint(1, 6)

        

class dice:
    def __init__(self):
        self.list = []
    
    def addDie(self, die): # Add a die to the list of dice
        self.list.append(die)
    
    def rollAll(self): # Roll all dice in the list
        for item in self.list:
            item.roll()