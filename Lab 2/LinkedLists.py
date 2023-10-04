class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
    
    def add(self, item):
        new_item = Node()
        new_item.data = item
        new_item.next = self.head.next
        self.head.next = new_item
    
    def delete(self):
        if self.head.next == None:
            return "Empty Linked List!"
        curr_node = self.head
        prev_node = None
        while curr_node.next is not None:
            prev_node = curr_node
            curr_node = curr_node.next
        if prev_node is not None:
            prev_node.next = None
            return curr_node.data
        else:
            self.head.next = None
            return curr_node.data

    def printList(self):
        curr_node = self.head.next
        while curr_node != None:
            print("data item", curr_node.data)
            curr_node = curr_node.next

test = LinkedList()
test.add(1)
test.add(2)
print("Deleted: ", test.delete())
print("Deleted: ",test.delete())
print(test.delete())
test.add(3)
test.add(4)
print("Deleted: ",test.delete())
test.add(5)
test.add(6)
test.printList()