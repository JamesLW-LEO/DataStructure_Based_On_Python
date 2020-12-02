class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 顺序删除
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head

    # step1: 获取链表长度
    cur, length = head, 0
    while cur:
        length += 1
        cur = cur.next

        # step2: 找到倒数第N个节点的前面一个节点
    cur = dummy
    for _ in range(length - n):
        cur = cur.next

    # step3: 删除节点，并重新连接
    cur.next = cur.next.next
    return dummy.next


# 回溯法
def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
    if not head:
        self.count = 0
        return head
    head.next = self.removeNthFromEnd(head.next, n)  # 递归调用
    self.count += 1  # 回溯时进行节点计数
    return head.next if self.count == n else head
