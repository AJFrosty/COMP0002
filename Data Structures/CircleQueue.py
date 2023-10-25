class CircularQueue:
    def __init__(self, max=3):
        self.__max = max
        self.__queue = [None]*max
        self.__back = -1
        self.__front = 0
        self.__items = 0
    
    def enqueue(self, item):
        if not self.isFull():
            if self.__back == (self.__max - 1):
                self.__back = -1
            self.__queue[self.__back + 1] = item
            self.__back += 1
            self.__items += 1
        else:
            print("Queue is Full")
    
    def dequeue(self):
        if not self.isEmpty():
            if self.__front == self.__max:
                self.__front = 0
            toDelete = self.__queue[self.__front]
            self.__queue[self.__front] = None
            self.__front += 1
            self.__items -= 1
            return toDelete
        return "Queue is Empty"
    
    def isEmpty(self):
        return self.__items == 0
    
    def isFull(self):
        return self.__items == self.__max
    
    def showQueue(self):
        print(self.__queue)
