# 中序遍历
"""
左   中   右
def inOrder(ptr):
    if ptr != None:
        inOrder(ptr.left)
        print(ptr.data)
        inOrder(ptr.right)
"""

# 后序遍历
"""
左   右   中
def postOrder(ptr):
    if ptr != None:
        postOrder(ptr.left)
        postOrder(ptr.right)
        print(ptr.data)
"""

# 前序遍历
"""
中   左   右
def preOrder(ptr):
    if ptr != None:
        print(ptr.data)
        preOrder(ptr.left)
        preOrder(ptr.right)
"""

