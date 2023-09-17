class Queue:
    def __init__(self, max = None) -> None:
        self.__queue = []
        self.__length = max

    def enqueue(self, item=''):
        self.__queue.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
            deleted = self.__queue[0]
            self.__queue.pop(0)
            return deleted
        print("Error: Queue is Empty!")
    
    def peek(self):
        if not self.isEmpty():
            return self.__queue[0]
        print("Error: Queue is Empty!")
    
    def isEmpty(self):
        return len(self.__queue) == 0
    
    def isFull(self):
        return len(self.__queue) == self.__length
    
    def search(self, item):
        return item in self.__queue
    

