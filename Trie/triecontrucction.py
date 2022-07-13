from pickle import TRUE


class SufixTrie:
    def __init_(self,string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrireForm(string)
        
    # O(n^2) time  / O (n^2) space 
    def populateSuffixTRieForm(self,string):
        for i in range(len(string)):
            self.insetSubstringStartingAt(i,string)

    def insetSubstringStartingAt(self,i,string):
        node = self.root
        for j in range(i,len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node [letter]
        node[self.endSymbol] = True

 # O(m) time / O(1) space

    def contains(self,string):
        node =  self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node

