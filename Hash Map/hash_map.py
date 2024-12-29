class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.hashList = [None]*self.size

    def add(self, key, value):
        index = self.getIndex(key)
        if self.hashList[index]:
            sublist = self.hashList[index]
            for pairs in sublist:
                if pairs[0] == key:
                    pairs[1] == value
                    return
            self.hashList[index].append([key, value])
        else:
            
            self.hashList[index] = [[key, value]]

    def getIndex(self, key):
        return hash(key)%self.size
    
    def get(self, key):
        index = self.getIndex(key)

        if self.hashList[index]:
            sublist = self.hashList[index]
            for pairs in sublist:
                if pairs[0] == key:
                    return pairs[1]
        return None
    
    def delete(self, key):
        index = self.getIndex(key)

        if self.hashList[index]:
            sublist = self.hashList[index]
            for i,pairs in enumerate(sublist):
                if pairs[0] == key:
                    del self.hashList[index][i]
                    return
        return "key not found"

dict = HashMap(10)
dict.add("name", "gokul")
dict.add("age", 21)
dict.add("gender", "male")

print(dict.get("name"))
print(dict.get("age"))
print(dict.get("gender"))
print(dict.get("occupation"))
print(dict.delete("gender"))