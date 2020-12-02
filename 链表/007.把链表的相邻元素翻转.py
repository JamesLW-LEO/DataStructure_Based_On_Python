class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    if head is None or head.next is None:
        return
    cur = head.next
    pre = head
    next = None  # 当前节点的后继节点的后继节点
    while cur is not None or cur.next is not None:
        # temp = cur.next
        next = cur.next.next
        pre.next = cur.next
        cur.next.next = cur
        cur.next = next
        pre = cur
        cur = next
    return head
