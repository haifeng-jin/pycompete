class Node:
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleList:
    
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def insert_before(self, old_node, data):
        new_node = Node(data, old_node.prev, old_node)
        new_node.prev.next = new_node
        new_node.next.prev = new_node
        

    def insert_after(self, old_node, data):
        new_node = Node(data, old_node, old_node.next)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
