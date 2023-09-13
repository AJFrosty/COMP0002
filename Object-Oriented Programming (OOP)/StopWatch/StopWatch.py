import time

class StopWatch:
    def __init__(self, startTime, endTime):
        self.__startTime = startTime
        self.__endTime = endTime

    def getStartTime(self):
        return self.__startTime
    
    def getEndTime(self):
        return self.__endTime
    
    def start(self):
        self.__startTime = time.time()
        return self.__startTime
    
    def stop(self):
        self.__stopTime = time.time()
        return self.__stopTime
    
    def getElapsedTime(self):
        elapsedTime = (self.__endTime - self.__startTime)* 1000
        return elapsedTime