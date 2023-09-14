class Fan:
    def __init__(self, speed = 1, radius = 5.0, color = 'blue', on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    
    def getSpeed(self):
        modes = ['SLOW', 'MEDIUM', 'FAST']
        current = modes[self.__speed - 1]
        return current
    def getRadius(self):
        return self.__radius
    def getColor(self):
        return self.__color
    def getOn(self):
        if self.__on and 1==1:
            return 'On'
        else:
            return 'Off'    
    def setSpeed(self,speed):
        self.__speed = speed
    def setRadius(self, radius):
        self.__radius = radius
    def setColor(self,color):
        self.__color = color
    def setOn(self, on):
        self.__on = on