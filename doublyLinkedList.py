class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
        self.tail = new_node

    def printBackward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> " if current.prev else "\n")
            current = current.prev

    def printForwards(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

    def peekHead(self):
        if self.head is None:
            print('The list is empty')
            return
        temp = self.head
        print('Head is', temp.data)

    def peekTail(self):
        if self.tail is None:
            print('The list is empty')
            return
        temp = self.tail
        print('Tail is:', temp.data)

    def popHead(self):
        if self.head is None:
            print('The list is empty')
            return
        if self.head == self.tail:
            print('The head is:', self.head.data, '\n')
            print('The list contains only one node and now its empty \n')
            self.head = None
            self.tail = None
        else:
            print('Popped Head:', self.head.data)
            self.head = self.head.next
            self.head.prev = None

    def popTail(self):
        if self.tail is None:
            print("The list is empty")
            return
        if self.tail == self.head:
            print('Popped Tail:', self.tail.data, '\n')
            print("The list is empty now")
            self.tail = None
        else:
            print("Popped Tail:", self.tail.data)
            self.tail = self.tail.prev
            self.tail.next = None

    def insertInbetween(self, key, pos):
        if self.head is None:
            print('The list is empty')
            return
        temp = self.head
        count = 1
        while temp and count < pos:
            count += 1
            temp = temp.next

        if temp is None:
            print("Position out of bounds")
            return

        newNode = Node(key)
        if temp.next is None:
            temp.next = newNode
            newNode.prev = temp
            self.tail = newNode
        else:
            next = temp.next
            temp.next = newNode
            newNode.prev = temp
            newNode.next = next
            next.prev = newNode


dll = DoublyLinkedList()
dll.insert(5)
dll.insert(10)
dll.insert(15)
dll.insert(20)
dll.insert(25)
dll.insert(30)

dll.peekHead()
dll.peekTail()

dll.popHead()

dll.peekHead()

dll.popTail()

dll.peekTail()

dll.insertInbetween(17, 4)
dll.printBackward()
print('\n')
dll.printForwards()
