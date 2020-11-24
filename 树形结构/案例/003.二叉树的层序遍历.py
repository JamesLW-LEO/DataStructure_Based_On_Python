"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

"""



def levelOrder(root):
    if root is None:
        return []
    levels = []
    from collections import deque
    # 定义队列
    queue = deque()
    # 最终的返回结果
    result = []
    # 先将根节点入队
    queue.append(root)
    while queue:
        # 记录当前队列的长度
        size = len(queue)
        # 临时列表存储每一层的节点
        cur_level = []
        for _ in range(size):
            # 出队
            node = queue.popleft()
            # 将当前值存储
            cur_level.append(node.val)
            # 当前值的左右节点非空时 入队
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(cur_level)
    return result
