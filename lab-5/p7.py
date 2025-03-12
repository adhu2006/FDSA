class DoublyNode:
    def __init__(self, data):
        self.data = data  # Node data
        self.next = None  # Reference to the next node in the list
        self.prev = None  # Reference to the previous node in the list

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty

    # Insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head.prev = new_node  # Set the previous of the current head to the new node
            self.head = new_node  # Move the head pointer to the new node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = DoublyNode(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Set the new node as the head
        else:
            last_node = self.head
            while last_node.next:  # Traverse to the last node
                last_node = last_node.next
            last_node.next = new_node  # Link the last node to the new node
            new_node.prev = last_node  # Set the previous pointer of the new node to the last node

    # Traverse the list forward and print the data of each node
    def traverse_forward(self):
        if self.head is None:  # If the list is empty
            print("The list is empty.")
            return
        current = self.head
        while current:  # Traverse until the end of the list
            print(current.data, end=" <-> " if current.next else "\n")
            current = current.next

# Example usage:
dll = DoublyLinkedList()

# Insert elements at the beginning
dll.insert_at_beginning(10)
dll.insert_at_beginning(20)

print("Doubly linked list after inserting 20, 10 at the beginning:")
dll.traverse_forward()

# Insert elements at the end
dll.insert_at_end(30)
dll.insert_at_end(40)

print("\nDoubly linked list after inserting 30, 40 at the end:")
dll.traverse_forward()

# Traverse the list forward
print("\nTraversing the doubly linked list forward:")
dll.traverse_forward()

