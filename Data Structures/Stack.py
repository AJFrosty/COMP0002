class Stack:
    def __init__(self, max =None):
        self.__stack = []
        self.__length = max

    def pop(self):
        if not self.isEmpty():
            deleted = self.__stack[-1]
            self.__stack.pop()
            return deleted
        print("Error: No Element is in the stack!")
    
    def push(self,item):
        if not self.isFull():        
            self.__stack.append(item)
        else:
            print("Error: Stack is FULL!")
    
    def peek(self):
        if not self.isEmpty():
            return self.__stack[-1]
        print("Error: No Element is in the stack!")
    
    def isEmpty(self):
        return len(self.__stack) == 0
    
    def isFull(self):
        return len(self.__stack) == self.__length
    
    def search(self, item):
        return item in self.__stack