""""This is a simple code that represents tree structure in programing"""
#To add => we iterate through the each node from root to last child
#         till we find a parentnode we want to add the data to 
#To remove => we iterate through each node in the tree till we find the 
#             data we wan to remove and then we remove it
#
#To display => to display the tree we use a empty quotation with depth 
#             zero and for every ege we increase the depth one and we print from left to right

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

class Tree:
    def __init__(self):
        self.root = None
    
    def addNode(self, data, parentdata=None):
        newNode = TreeNode(data)
        if not self.root:
            self.root = newNode
            return
        ParentNode = self.findNode(parentdata, self.root)

        if ParentNode:
            ParentNode.children.append(newNode)
    
    def findNode(self, data, node):
        if node.data == data:
            return node
        for child in node.children:
            nodeFound = self.findNode(data, child)
            if nodeFound:
                return nodeFound
        return None
    
    def remove(self, data):
        if not self.root:
            print("tree is empty")
            return
        ParentNode = self.findParentNode(self.root, data)

        if ParentNode:
            for child in ParentNode.children:
                if child.data == data:
                    ParentNode.children.remove(child)
    
    def findParentNode(self, node, data):
        for child in node.children:
            if child.data == data:
                return node
            nodeFound = self.findParentNode(child, data)
            if nodeFound:
                return node
        return None
    
    def display(self, depth=0, node=None):
        if not node:
            node = self.root
        

        print(" "*depth, node.data)

        for child in node.children:
            self.display(depth+1, child)


tree = Tree()

tree.addNode(1)
tree.addNode(2, 1)
tree.addNode(3, 1)
tree.addNode(4, 2)
tree.addNode(5, 2)
tree.addNode(6, 3)
tree.addNode(7, 3)

tree.display()


tree.remove(3)

tree.display()