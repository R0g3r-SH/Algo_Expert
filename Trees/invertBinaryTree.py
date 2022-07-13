from tkinter.tix import Tree


#0n time o(d) space d is the depth in the tree


def invertBinaryTree(tree):
    if tree is None:
        return
    swap(tree)
    invertBinaryTree(tree.rigth)
    invertBinaryTree(tree.left)


def swap (tree):
    tree.left,tree.rigth = tree.rigth,tree.left