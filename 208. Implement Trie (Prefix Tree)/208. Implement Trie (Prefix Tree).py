class TrieNode:
    def __init__(self):
        self.children = [0]*26
        self.isWord = False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()
    
    def getNode(self):
        return TrieNode()
    
    def getIndex(self, ch):
        if 'a'<=ch<='z':
            return ord(ch) - ord('a')
        else:
            return ord(ch) - ord('A')

    def insert(self, word: str) :
        """
        Inserts a word into the trie.
        """
        marker = self.root
        
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not marker.children[index]:
                marker.children[index] = self.getNode()
            marker = marker.children[index]           
        
        marker.isWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        marker = self.root
        
        for i in range(len(word)):
            index = self.getIndex(word[i])
            if not marker.children[index]:
                return False
            marker = marker.children[index]
        
        return marker is not None and marker.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        marker = self.root
        
        for i in range(len(prefix)):
            index = self.getIndex(prefix[i])
            if not marker.children[index]:
                return False
            marker = marker.children[index]
        
        return marker is not None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)