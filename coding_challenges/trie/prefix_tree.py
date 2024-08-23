# Trie(Prefix Tree)

# Insert Word: 0(1)
# Search word: 0(1)
# Search Prefix: 0(1) - For example the word "apple" has the prefix "ap".

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True 

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.word

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
    

trie = Trie()
trie.insert("apple")
trie.insert("ape")
trie.insert("bananas")
print(trie.search("apple"))
