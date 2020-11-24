"""
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
  一.若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
  二.若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
  三.它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树
"""
from 树形结构.案例.tree import TreeNode


def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None
    length = len(nums)
    mid = length // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root


print(sortedArrayToBST([-10, -3, 0, 5, 9]))
