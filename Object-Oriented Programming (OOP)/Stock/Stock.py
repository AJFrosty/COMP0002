class Stock:
    def __init__(self, symbol: str, name: str, previousClosingPrice: float, currentPrice: float):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name
    
    def getSymbol(self):
        return self.__symbol
    
    def previousClosingPrice(self):
        return self.__previousClosingPrice
    
    def setPreviousClosingPrice(self, price):
        self.__previousClosingPrice = price

    def getCurrentPrice(self):
        return self.__currentPrice
    
    def setCurrentPrice(self, price):
        self.__currentPrice = price

    def getChangePercentage(self):
        diff = self.__currentPrice - self.__previousClosingPrice
        diff = diff/self.__previousClosingPrice
        diff = diff * 100
        return diff