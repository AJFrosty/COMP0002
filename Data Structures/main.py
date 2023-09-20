from Queue import Queue
from Stack import Stack

stack = Stack(5)
queue = Queue(5)

for i in range(1,7):
    stack.push(i**2)
    queue.enqueue(str(i**3))

queue.dequeue()

item_1 = stack.search(16)
item_2 = queue.search('8')
print("\n---------------------------------------------------------------------")
print(f"Stack \nFull Stack: {stack.isFull()} \nEmpty Stack: {stack.isEmpty()} \nTop Stack: {stack.peek()} \n16 In Stack: {item_1} \n")
print("---------------------------------------------------------------------")
print(f"Queue \nFull Queue: {queue.isFull()} \nEmpty Queue: {queue.isEmpty()} \nNext in Queue: {queue.peek()} \n8 In Stack: {item_2}")
