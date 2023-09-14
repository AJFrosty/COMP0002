import time

class StopWatch:
    def __init__(self, startTime, endTime):
        self.__startTime = startTime
        self.__endTime = endTime

    def getStartTime(self):
        return time.strftime("%H:%M:%S", time.localtime(self.__startTime))
    
    def getEndTime(self):
        return time.strftime("%H:%M:%S", time.localtime(self.__endTime))
    
    def start(self, time):
        self.__startTime = time
    
    def stop(self, time):
        self.__endTime = time
    
    def getElapsedTime(self):
        elapsedTime = (self.__endTime - self.__startTime) * 1000
        return elapsedTime
