class Pizza:
    def __init__(self, size):
        if size == "S":
            self.size = size
            self.price = 0.0
        if size == "M":
            self.size = size
            self.price = 0.0
        if size == "L":
            self.size = size
            self.price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
    
    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size

