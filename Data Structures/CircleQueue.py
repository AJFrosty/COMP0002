class CircularQueue:
    def __init__(self, max=3):
        self.__max = max
        self.__queue = [None] * 3
        self.__back = -1
        self.__front = 0
        self.__items = 0
    
    def enqueue(self, item):
        if not self.isFull():
            if self.__back == 2:
                self.__back = -1
            self.__queue[self.__back + 1] = item
            self.__back += 1
            self.__items += 1
        else:
            print("Queue is full!")
    
    def dequeue(self):
        if not self.isEmpty():
            toDelete = self.__queue[self.__front]
            self.__queue[self.__front] = None
            self.__front += 1
            self.__items -= 1
            return toDelete
        return "Queue is empty!"

    def isEmpty(self):
        return self.__back == -1
    
    def isFull(self):
        return self.__items == self.__max
    
    def showQueue(self):
        print(self.__queue)

q = CircularQueue(3)
q.enqueue(40)
q.showQueue()
q.enqueue(10)
q.showQueue()
q.enqueue(5)
q.showQueue()
q.enqueue(30)
q.showQueue()
q.dequeue()
q.showQueue()
q.dequeue()
q.showQueue()
q.enqueue(33)
q.showQueue()
q.dequeue()
q.showQueue()