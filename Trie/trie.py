class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        currentNode = self.root

        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
        currentNode.IsEnd = True

    def search(self, word):
        currentNode = self.root

        for char in word:
            if char not in currentNode.children:
                return False
            currentNode = currentNode.children[char]
        if currentNode.IsEnd == True:
            return True
        return False

    def remove(self, word):
        if not self.search(word):
            print("No word Found")
            return
        
        stack =[]
        currentnode = self.root
        for char in word:
            stack.append(currentnode)
            currentnode = currentnode.children[char]
        currentnode.IsEnd = False

        while len(stack)>0:
            node = stack.pop()
            char = word[len(stack)]

            if not node.children[char].IsEnd and not node.children[char].children:
                del node.children[char]
            else:
                break
        print("Word Removed")

trie = Trie()

trie.add("GO")
trie.add("GOLD")
trie.add("GOOD")
print(trie.search("GOODS"))

trie.remove("GOLD")