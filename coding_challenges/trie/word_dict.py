class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
        

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children and char != '.':
                return False
            if char != '.':
                curr = curr.children[char]
        return True
    

wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
# print(wordDictionary.search("pad"))
# print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
# print(wordDictionary.search("b.."))