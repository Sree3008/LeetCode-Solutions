class Node:
    def __init__(self,x):
        self.dt = {}
        self.val = x
        self.end = False

class Trie:

    def __init__(self):
        self.root = Node(None)
        
    def insert(self, word: str) -> None:
        temp= self.root
        for i in word:
            if i in temp.dt:
                temp = temp.dt[i]
            else:
                temp.dt[i] = Node(i)
                temp = temp.dt[i]
        temp.end= True

    def search(self, word: str) -> bool:
        temp = self.root
        for i in word:
            if i in temp.dt:
                temp = temp.dt[i]
            else:
                break
        else:
            return temp.end
        return False

    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for i in prefix:
            if i in temp.dt:
                temp = temp.dt[i]
            else:
                break
        else:
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

