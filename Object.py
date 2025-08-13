class product:
    def __init__(self, name, price,discountpercent): # Initialize product with name, price, and discount percent
        self.name = name
        self.price = price
        self.discountpercent = discountpercent

        def descountamount(self): # Calculate the discount amount based on the price and discount percent
            return self.price * (self.discountpercent / 100)

        def discountedprice(self): # Calculate the discounted price by subtracting the discount amount from the original price
            return self.price - self.descountamount()

        def getdescription(self): # Print the product details including name, price, discount percent, discount amount, and discounted price
            print("name:", self.name)
            print("price:", self.price)
            print("discount percent:", self.discountpercent)

        def __str__(self): # String representation of the product details
            return f"name:{self.name}\nprice:{self.price}\n discount percent:{self.discountpercent}\ndiscount amount:{self.descountamount()}\ndiscounted price:{self.discountedprice()}"
                   