class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return

        self.recursiveAdd(data , self.root)
    def recursiveAdd(self, data, node):
        if not node.left:
            node.left = Node(data)
        elif not node.right:
            node.right = Node(data)
        else:
            self.recursiveAdd(data, node.left)

    def display(self, depth=0, node=None):
        if node is None:
            node = self.root
        
        print(" "*depth, node.data)

        if node.left is not None:
            self.display(depth+1, node.left)
        if node.right is not None:
            self.display(depth+1, node.right)

tree = BinaryTree()

tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)

tree.display()