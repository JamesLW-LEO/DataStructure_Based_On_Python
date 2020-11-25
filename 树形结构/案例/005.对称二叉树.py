"""
给定一个二叉树，检查它是否是镜像对称的。

# 递归大法

"""


def isSymmetric(root):
    if not root:
        return None
    return auxiliary(root.left, root.right)


def auxiliary(leftNode, rightNode):
    if not leftNode and not rightNode:
        return True
    if not leftNode and rightNode:
        return False
    if leftNode and not rightNode:
        return False
    if leftNode.val != rightNode.val:
        return False
    else:
        return auxiliary(leftNode.left, rightNode.right) and auxiliary(leftNode.right, rightNode.left)
