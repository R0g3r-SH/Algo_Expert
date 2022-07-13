from pandas import array


class Node:
    def __init(self,name):
        self.children = []
        self.name = name

    def addChild(self,name):
        self.children.append(Node(name))
    
    def depthFirstSearch(self,name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearsh(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array

