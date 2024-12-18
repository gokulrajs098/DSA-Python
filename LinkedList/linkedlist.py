class Node:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.pointer is not None:
                curr = curr.pointer
            curr.pointer = newNode
    
    def print(self):
        if self.head is None:
            print("linked list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.value, end="->",)
                curr = curr.pointer
    
    def remove(self, value):
        if self.head is not None:
            if self.head.value == value:
                self.head = self.head.pointer
            else:
                curr = self.head
                while curr.pointer is not None and curr.pointer.value != value:
                    curr = curr.pointer
                if curr.pointer is not None:
                    curr.pointer = curr.pointer.pointer
                else:
                    print(value, "value not found in linked list")
        else:
            print("linked lsit is empty")


linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.add(6)

linkedList.print()

linkedList.remove(5)

linkedList.print()


