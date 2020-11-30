# 单链表反转
# from .*.001.建立单向链表 import createLinkList

def reverseList(head):
    """
    leetcode官方解法，思路和上一个解法大同小异，重点是在第1个节点前构造一个虚拟节点
    """
    if head is None or head.next is None:  # 兼容leetcode特殊用例，链表为空或只有1个节点
        return head
    pre_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next  # 暂存当前节点的next节点
        current_node.next = pre_node   # 当前节点的next指向初始化的节点
        pre_node = current_node        # 初始化的节点为当前节点
        current_node = next_node       # 当前节点为暂存的节点
    return pre_node