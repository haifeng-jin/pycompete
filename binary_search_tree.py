class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def lower_bound(self, value):
        node = self.root
        ret = None
        while node is not None:
            if value < node.val:
                ret = node.val
                node = node.left
            elif value == node.val:
                return node.val
            else:
                node = node.right
        return ret
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        last_node = None
        node = self.root
        while node is not None:
            last_node = node
            if value < node.val:
                node = node.left
            else:
                node = node.right
                
        if value < last_node.val:
            last_node.left = Node(value)
        else:
            last_node.right = Node(value)
