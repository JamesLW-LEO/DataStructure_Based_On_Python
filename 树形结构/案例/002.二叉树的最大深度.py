"""
题目
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9   20
     /  \
    15   7
"""
from .tree import TreeNode


# 方法一 递归
def maxDepth(root):
    '''
    使用递归的方式
    :param root:
    :return:
    '''
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


# 方法二 广度优先搜索
'''
这里，我们需要添加一个辅助队列。我们将当前层的所有节点都存入这个辅助队列中。
在这里需要注意一点，当我们准备搜索下一层时，这里需要将队列中当前层的所有节点都进行出队，然后让这些节点往下层搜索。
那么，如果当前层的所有节点都出列，队列还非空，那么说明下一层还有节点。循环直至队列为空，
定义变量 depth，每层搜索的时候维护更新该值，那么最终，depth 就是我们要求的二叉树最大深度。
'''


def maxDepth2(root):
    if not root:
        return 0
    from collections import deque
    queue = deque()
    depth = 0
    queue.append(root)
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth


maxDepth2([3, 9, 20, '', '', 15, 7])
