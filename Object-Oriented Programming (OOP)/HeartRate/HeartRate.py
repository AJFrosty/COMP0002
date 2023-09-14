from datetime import datetime as dt

class HeartRates:
    def __init__(self, first, last, month, day, year):
        self.firstName = first
        self.lastName = last
        self.month = month
        self.day = day
        self.year = year
    
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
    def getMonth(self):
        return self.month
    def getDay(self):
        return self.day
    def getYear(self):
        return self.year
    
    def setFirstName(self,first):
        self.firstName = first
    def setLastName(self,last):
        self.lastName = last
    def setMonth(self, month):
        self.month = month
    def setDay(self, day):
        self.day = day
    def setYear(self, year):
        self.year = year
    
    def age(self):
        birth = dt(self.year, self.month, self.day)
        today = dt.now()
        currentAge = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return currentAge
    
    def maxHeartRate(self):
        hr = 220 - self.age()
        return hr
    
    def targetHeartRate(self):
        fifty = 0.5 * self.maxHeartRate()
        eightyFive = 0.85 * self.maxHeartRate()
        return f"{fifty} to {eightyFive}"
    
    
        
