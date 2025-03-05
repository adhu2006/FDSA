class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next
        if not temp:
            return
        prev.next = temp.next
        temp = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example usage:
linked_list = SinglyLinkedList()

# Insert at beginning
linked_list.insert_at_beginning(10)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(30)
linked_list.traverse()

# Insert at end
linked_list.insert_at_end(5)
linked_list.insert_at_end(10)
linked_list.insert_at_end(15)
linked_list.insert_at_end(20)
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.traverse()

# Delete node with data 20
linked_list.delete_node(20)
linked_list.traverse()

