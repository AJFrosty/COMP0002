class Account:
    def __init__(self, id=0, balance=100.0, annualInterestRate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate
    
    def getId(self):
        return self.__id
    
    def getBalance(self):
        return self.__balance
    
    def getAnnualInterestRate(self):
        return self.__annualInterestRate
    
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 100)/12
    
    def setId(self, id):
        self.__id = id
    
    def setBalance(self, balance):
        self.__balance = balance
    
    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate
    
    def getMonthlyInterest(self):
        monthly = (self.__annualInterestRate / 100)/12
        interest = self.__balance * monthly
        return interest
    
    def withdraw(self, ammount):
        if ammount <= self.__balance:
            newBal = self.__balance - ammount
            self.__balance = newBal

    def deposit(self, ammount):
        self.__balance += ammount