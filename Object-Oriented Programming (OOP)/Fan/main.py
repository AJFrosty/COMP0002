from Fan import Fan

myFan = Fan(3,10,'yellow',True)
newFan = Fan(2,5,'blue',False)

print(f"The Fan is {myFan.getOn()} \nCurrent Speed: {myFan.getSpeed()} \nMax Radius: {myFan.getRadius()} \nFan Color: {myFan.getColor()}")
print(f"The Fan is {newFan.getOn()} \nCurrent Speed: {newFan.getSpeed()} \nMax Radius: {newFan.getRadius()} \nFan Color: {newFan.getColor()}")