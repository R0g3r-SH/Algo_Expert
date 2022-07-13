#this solve Better with recursion
# 0(n) Time | 0(h) space were h is the heith of the tree

def nodeDepths(root ,depth = 0):
    #base case 
    if root is None:
        return root
    return depth + nodeDepths(root.left,depth+1) + nodeDepths(root.rigth,depth+1)