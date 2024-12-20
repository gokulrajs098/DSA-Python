class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BSTree:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        if not self.root:
            self.root = BinaryTree(data)
        
        self.recursiveadd(data, self.root)
        
    def recursiveadd(self, data, node):
        if data < node.data:
            if not node.left:
                node.left = BinaryTree(data)
            else:
                self.recursiveadd(data, node.left)
        elif data > node.data:
            if not node.right:
                node.right = BinaryTree(data)
            else:
                self.recursiveadd(data, node.right)
    
    def inordertraversal(self):
        result = []
        self.recursiveinordertraveral(self.root, result)
        print(result)

    def recursiveinordertraveral(self, node, result):
        if not node:
            return None
        else:
            self.recursiveinordertraveral(node.left, result)
            result.append(node.data)
            self.recursiveinordertraveral(node.right, result)


    def preordertraversal(self):
        result = []
        self.recursivepreordertraversal(self.root, result)
        print(result)
    
    def recursivepreordertraversal(self, node, result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.recursivepreordertraversal(node.left, result)
            self.recursivepreordertraversal(node.right, result)

    def postordertraversal(self):
        result = []
        self.recursivepostordertraversal(self.root, result)
        print(result)
    
    def recursivepostordertraversal(self, node, result):
        if not node:
            return None
        else:
            
            self.recursivepostordertraversal(node.left, result)
            self.recursivepostordertraversal(node.right, result)
            result.append(node.data)

    def remove(self, data):
        if not self.root:
            print("Binary tree is empty")
        
        self.recursiveRemove(data, self.root)

    def recursiveRemove(self, data, node):
        if node.left and node.left.data == data:
            node.left = None
            return
        elif node.right and node.right.data == data:
            node.right = None
            return
        elif data < node.data:
            self.recursiveRemove(data, node.left)
        elif data > node.data:
            self.recursiveRemove(data, node.right)

    def search(self, data):
        node = self.recursiveSearch(data, self.root)
        if node:
            print("True")
        else:
            print("False")
    def recursiveSearch(self, data,  node):
        if node and node.data == data:
            return node
        elif data < node.data:
            self.recursiveSearch(data, node.left)
        elif data > node.data:
            self.recursiveSearch(data, node.right)

bst = BSTree()
bst.add(2)
bst.add(1)
bst.add(3)
bst.add(4)
bst.add(5)
bst.add(6)

bst.inordertraversal()

bst.preordertraversal()

bst.postordertraversal()

bst.remove(4)

bst.inordertraversal()

bst.search(1)
