class Invoice:
    def __init__(self, partNumber, partDescription, quantity, price):
        self.partNumber = partNumber
        self.partDescription = partDescription
        self.quantity = quantity
        self.price = price
    
    def getPartNumber(self):
        return self.partNumber
    def getPartDescription(self):
        return self.partDescription
    def getQuantity(self):
        return self.quantity
    def getPrice(self):
        if self.price < 0:
            return 0.0
        else:
            return self.price
    
    def setPartNumber(self, partNumber):
        self.partNumber = partNumber
    def setPartDescription(self, partDescription):
        self.partDescription = partDescription
    def setQuantity(self, quantity):
        self.quantity = quantity
    def setPrice(self, price):
        self.price = price

    def getInvoiceAmount(self):
        amount = self.getPrice() * self.getQuantity()
        if amount < 0:
            return 0
        else:
            return amount