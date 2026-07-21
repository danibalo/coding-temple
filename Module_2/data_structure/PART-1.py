
class Node:
    """A single node in linkedlist"""
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"Node ({self.value})"
class LinkedList:
    """A singly linked list"""
    def __init__(self):
        self.head = None # No node yet
    def insert_at_beginning(self, value):
        """Add a new node at the front of the list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, value):
        """ Add a new node at the end of list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        print("->".join(elements) + "-> None")
    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            return False
    def delete(self, target):
        """Remove the first node with the given value. Return True if found, False if not."""
        #empty list
        if self.head == None:
            return False
        # When the head contains the target
        if self.head == target:
            self.head = self.head.next
            return True
        #search for the target
        current = self.head
        while current.next:
            if current.next.value == target:
                current.next = current.next.next
                return True
            current = current.next
    def length(self):
        """Return the number of nodes in the list. O(n) time."""
        if self.head == None:
            return 0
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def to_list(self):
        """Convert the linked list to a Python list. Returns a list of values."""
        converted_to_list = []
        current = self.head
        while current:
            converted_to_list.append(current.value)
            current = current.next
        return converted_to_list



    

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

ll = LinkedList()
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)

print("The Linked list:")
ll.display()           # 10 -> 20 -> 30 -> 40 -> 50 -> None
print(f"Length of linked list: {ll.length()}")     # 5
ll.delete(30)
print("After 30 is deleted")
ll.display()           # 10 -> 20 -> 40 -> 50 -> None
print("Linked list converted to python list")
print(ll.to_list())    # [10, 20, 40, 50]
