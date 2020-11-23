# 插入
"""
二叉树查找：
def search(ptr,val):
    while True:
        if ptr is None:
            return None
        if ptr.data == val:
            return ptr
        elif ptr.data >val:
            ptr = ptr.left
        else:
            ptr = ptr.right
"""


class Tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None


def createTree(root, val):
    """
    创建一个二叉树
    :param root:
    :param val:
    :return:
    """
    newnode = Tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None
    if root is None:
        root = newnode
        return root
    else:
        current = root
        while current is not None:
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


def search(root, val):
    i = 1
    while True:
        if root is None:
            return None
        if root.data == val:
            print("查找了{0}次".format(i))
            return root
        elif root.data > val:
            root = root.left
        else:
            root = root.right
        i += 1


def inorder(root):
    if root is not None:
        inorder(root.left)
        print("[%2d]" % root.data, end=" ")
        inorder(root.right)


if __name__ == '__main__':
    data = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
    root = None
    for i in range(11):
        root = createTree(root, data[i])
    target = int(input("请输入查找的数值"))
    if search(root, target) is not None:
        print("找到了")
    else:
        print("NO NO ...没找到")
        print("准备插入")
        root = createTree(root, target)
        inorder(root)

# 删除
"""
存在三种情况：
1.删除的节点为树叶，只要将其相连的父节点指向None
2.删除的节点只有一棵子树，
3.删除的节点有两棵子树
    找出中序立即先行者 即将欲删除节点的左子树中最大者往上提 该节点的左子树往右找 直到右指针指向None
    找出中序立即后继者 即将欲删除节点的右子树中最小者往上提 该节点的右子树往左找 直到左指针指向None
"""
