#Double LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    def __repr__(self):
        return f"Node{self.value}"
class LinkedList:
    """A doubly linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_at_beginning(self, value):
        """ Add new node at beginning of the list """
        new_node = Node(value)
        #Empty list
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return 
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def insert_at_end(self, value):
        """ Add new node at end of the list """
        new_node = Node(value)
        #Empty list
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    def display_reverse(self):
        """ Display the list in reverse"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.value))
            current = current.prev

        print(' -> '.join(elements) + ' -> None')
ll = LinkedList()

for value in [10, 20, 30, 40, 50]:
    ll.insert_at_end(value)

ll.display_reverse()