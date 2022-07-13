#0n time o(d) space d is the depth in the tree
#recursive metod

def validateBST (tree):
    return validatehelpelper(tree,float("-inf"),float("-float"))


def validatehelpelper (tree, minv, maxv):
    #base case 
    if tree is None:
        return True
    
    if tree.value <minv or tree.value >= maxv:
        return False

    return  validatehelpelper(tree.left, minv,tree.value) and  validatehelpelper(tree.left, minv,tree.value)