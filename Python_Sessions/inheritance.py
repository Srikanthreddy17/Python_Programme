class product:
    def __init__(self, name="", price=0.0, discountpercent=0.0):
        self.name = name
        self.price = price
        self.discountpercent = discountpercent
        
        def discountamount(self):
            return self.price * (self.discountpercent / 100)
        
        def discountedprice(self):
            return self.price - self.getdiscountamount()
        
        def getdescription(self):
            return self.name
    
    
class book(product):    # Inherit from product class
    # Initialize book with name, price, discount percent, and author
    def __init__(self, name="", price=0.0, discountpercent = 0.0, author=""):
           super().__init__(name, price, discountpercent)
           self.author = author

           def getdescription(self):
               return product.getdescription(self) + " by " + self.author
           
class movie(product):  # Inherit from product class
    # Initialize movie with name, price, discount percent, and director
    def __init__(self, name="", price=0.0, discountpercent=0.0, year=1997):

        def getdescription(self):
            return product.getdescription(self) + " year " + str(self.year)