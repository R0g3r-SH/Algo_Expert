from inspect import stack


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    stack = []
    helper = (root,stack,0)
    return stack

def helper(root,stack,sum):
    if root is None:
        return
    newsum = sum + root.value
    if root.left is None and root.right is None:
        stack.append(newsum)
    helper (root.left,stack,newsum)
    helper(root.rigth,stack,newsum)