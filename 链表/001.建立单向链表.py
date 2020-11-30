# 建立链表  遍历链表

class student():
    def __init__(self):
        self.next = None
        self.data = None


def createLinkList(n):
    i = 1
    head = student()
    head.next = None
    new_data = None
    ptr = head
    while i < n:
        new_data = student()
        new_data.data = i
        new_data.next = None
        ptr.next = new_data
        ptr = new_data
        i += 1
    return head


def printLinkList(root):
    ptr = root.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next


# root = createLinkList(4)
# print(printLinkList(root))


if __name__ == '__main__':
    i = 1
    head = student()
    head.next = None
    new_data = None
    ptr = head
    while i < 4:
        new_data = student()
        new_data.data = i
        new_data.next = None
        ptr.next = new_data
        ptr = new_data
        i += 1
    ptr = head.next
    while ptr != None:
        print(ptr.data)
        ptr = ptr.next