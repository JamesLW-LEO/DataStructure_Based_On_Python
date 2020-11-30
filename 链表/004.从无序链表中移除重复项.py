class LNode(object):
    def __init__(self, item):
        self.data = item
        self.next = None


# 顺序删除  时间复杂度  o(n**2)
def removeDup(head):
    if head == None or head.next == None:
        return
    outerCur = head.next
    interCur = None
    interPre = None
    while outerCur != None:
        interCur = outerCur.next
        interPre = outerCur
        while interCur != None:
            if outerCur.data == interCur.data:
                interPre.next = interCur.next
                interCur = interPre.next
            else:
                interPre = interCur
                interCur = interCur.next
        outerCur = outerCur.next


# 空间换时间
"""
建立一个列表保存已经遍历过的节点值
从头节点开始遍历链表 如果节点内容不在列表中 那么继续遍历 如果存在 就删除
"""


def removeDup2(head):
    if head is None or head.next is None:
        return
    cur = head.next
    pre = None
    hashList = []

    while cur is not None:
        if cur.data in hashList:
            pre.next = cur.next
            cur = pre.next
        else:
            hashList.append(cur.data)
            pre = cur
            cur = cur.next


if __name__ == "__main__":
    i = 1
    head = LNode(0)
    head.next = None
    tmp = None
    cur = head
    while i < 7:
        tmp = LNode(i)
        if i % 2 == 0:
            tmp.data = i + 1
        elif i % 3 == 0:
            tmp.data = i - 2
        else:
            tmp.data = i
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    print("删除重复节点前：")
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next
    removeDup2(head)
    print("删除节点后：")
    cur = head.next
    while cur != None:
        print(cur.data)
        cur = cur.next
