class Rectangle:
    def __init__(self, w=1, h=2):
       self.width = w
       self.height = h

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (2*self.width) + (2*self.height)

    def printRectangle(self):
        print(f"Width: {self.width}")
        print(f"height: {self.height}")
        print(f"Area: {self.getArea()}")
        print(f"Perimeter: {self.getPerimeter()}")

