# 列表实现
class StackArray():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    # 返回栈顶元素
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None

    # 弹栈
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            print("栈已为空")
            return None

    def push(self, item):
        self.items.append(item)


# 链表
class LNode():
    def __init__(self):
        self.data = None
        self.next = None


class StackLinklist():
    def __init__(self):
        self.data = None
        self.next = None

    def empty(self):
        if self.next is None:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.next
        while p != None:
            p = p.next
            size += 1
        return size

    def push(self, e):
        p = LNode()
        p.data = e
        p.next = self.next
        self.next = p

    def pop(self):
        '''
        出栈
        :return:
        '''
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
            return tmp.data
        return "栈已空"

    def top(self):
        '''
        取栈顶元素
        :return:
        '''
        if self.next is not None:
            return self.next.data
        return "栈已空"
