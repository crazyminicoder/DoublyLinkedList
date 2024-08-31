class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def printBackward(self):
        current = self.head
        while current.next:
            current = current.next
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev


dll = DoublyLinkedList()
dll.insert(5)
dll.insert(10)
dll.insert(15)
dll.insert(20)
dll.insert(25)
dll.insert(30)

dll.printBackward()
