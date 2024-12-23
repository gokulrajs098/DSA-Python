class HeapNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Heap:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = HeapNode(data)
            return
        
        self.recursive_add(data, self.root)
    
    def recursive_add(self, data, node):
        if not node.left:
            node.left = HeapNode(data)
        elif not node.right:
            node.right = HeapNode(data)
        else:
            if self.get_count(node.left) <= self.get_count(node.right):
                self.recursive_add(data, node.left)
            else:
                self.recursive_add(data, node.right)
        
    def get_count(self, node):
        if not node:
            return 0
        
        return 1 + self.get_count(node.left) + self.get_count(node.right)
    
    def heapify_up(self, node):
        
        while node and node != self.root:
            parent_node = self.get_parent(node, self.root)
            if parent_node.data > node.data:
                parent_node.data, node.data = node.data, parent_node.data
                node = parent_node
            else:
                break
    

    def get_parent(self, node, root):
        if root.left == node or root.right == node:
            return root
        if root.left:
            parent = self.get_parent(node, root.left)
            if parent:
                return parent
        if root.right:
            parent = self.get_parent(node, root.right)
            if parent:
                return parent
        return None

    def extract_min(self):
        if not self.root:
            return
        min = self.root.data
        last_node_value  = self.remove_last_node()

        if last_node_value:
            self.root.data = last_node_value
            self.heapify_down(self.root)
        else:
            self.root = None
        return min
    
    def remove_last_node(self):
        queue = [self.root]
        last_node = None
        while len(queue) != 0:
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            if not curr.left and not curr.right:
                last_node = curr
        if last_node:
            parent_node = self.get_parent(last_node, self.root)
            if parent_node.left == last_node:
                parent_node.left = None
            else:
                parent_node.right = None
            return last_node.data
        return None
    
    def heapify_down(self, node):
        while node:
            small = node
            if node.left and node.left.data < small.data:
                small = node.left
            if node.right and node.right.data < small.data:
                small = node.right
            if small != node:
                small.data, node.data = node.data, small.data
                node = small
            else:
                break

heap = Heap()

heap.add(7)
heap.add(6)
heap.add(5)
heap.add(4)
print(heap.extract_min())
print(heap.extract_min())
print(heap.extract_min())