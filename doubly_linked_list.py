class Node:
    
    def __init__(self, data):
        self.data = data
        self.before = None
        self.next = None
    

class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, x):
        node = Node(x)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            node.next.before = self.head

    def delete(self, x):
        node = self.head
        while node is not None:
            if node.data == x:
                if node.before is None:
                    self.head = self.head.next
                    self.head.before = None
                else:
                    node.before.next = node.next
                
                if node.next is None:
                    self.tail = self.tail.before
                    self.tail.next = None
                else:
                    node.next.before = node.before

                break
            node = node.next

    def deleteFirst(self):
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.before = None

    def deleteLast(self):
        if self.tail.before is None:
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.before
            self.tail.next = None

    def show(self):
        ret = []
        node = self.head
        while node is not None:
            ret.append(node.data)
            node = node.next
        print()


ll = Linked_List()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'insert':
        ll.insert(command[1])
    elif command[0] == 'delete':
        ll.delete(command[1])
    elif command[0] == 'deleteFirst':
        ll.deleteFirst()
    else:
        ll.deleteLast()

ll.show()
