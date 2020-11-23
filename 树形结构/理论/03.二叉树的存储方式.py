# 二叉查找树的特点
"""
可以是空集合 但若不是空集合 则节点上一定要有一个键值
每一个树根的值需大于左子树的值
每一个树根的值需小于右子树的值
左右子树也是二叉查找树
树的每一个节点的值都不相同
"""


# 数组的方式存储
def treeCreateByArray(btree, data, length):
    for i in range(1, length):
        level = 1
        while btree[level] != 0:
            if data[i] > btree[level]:  # 如果数组内的值大于树根 就往右子树比较
                level = level * 2 + 1
            else:
                level = level * 2
        btree[level] = data[i]
    return btree


# 链表的存储方式
class tree():
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def treeCreateByLinkList(root, val):
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None
    if root == None:
        root = newnode
        return root
    else:
        current = root
        while current != None:
            backup = current
            if current.data > val:
                current = current.left
            else:
                current = current.right
        if backup.data > val:
            backup.left = newnode
        else:
            backup.right = newnode
    return root
