class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False



class Trie(object):


    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root #Makes the top node the root
        for Character in word:  #iterares over every character
            if Character not in node.children:
                node.children[Character] = TrieNode() #makes a new node for the new character
            node = node.children[Character] # else makes the new node the root node
        node.is_word = True

    def search(self,word):
        node = self.root #gets the root node
        for Character in word:
            if Character not in node.children:
                return False #returns false in charcetr not in node
            node = node.children[Character] # else it makes the found node the new root node

        return node.is_word # after its finished it returns true as the word is in there

    def startsWith(self, prefix):
        node = self.root #gets the root node
        for Character in prefix: # same thing as seach() but just with prefix
            if Character not in node.children:
                return False
            node = node.children[Character]
        return True
