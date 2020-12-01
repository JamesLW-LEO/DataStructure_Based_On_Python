class LNode(object):
    def __init__(self, item):
        self.data = item
        self.next = None


def findLastK(head, k):
    if head is None or head.next is None:
        return
    slow = LNode()
    fast = LNode()
    slow = head.next
    fast = head.next
    i = 1
    while fast is not None:
        fast = fast.next
        i += 1
        if i > k:
            break
    else:
        return None
    # fast指向第k个元素
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow
