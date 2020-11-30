# 数组实现
class Queue():
    def __init__(self):
        self.arr = []
        self.front = 0  # 队列头
        self.rear = 0  # 队列尾

    def isEmpty(self):
        return self.front == self.rear

    def size(self):
        return self.rear - self.front

    def getFront(self):
        '''
        返回队列首元素
        :return:
        '''
        if self.isEmpty():
            return None
        return self.arr[self.front]

    def getBack(self):
        '''
        返回队尾元素
        :return:
        '''
        if self.isEmpty():
            return None
        return self.arr[self.rear - 1]

    def deQueue(self):
        '''
        删除队列头元素
        :return:
        '''
        if self.rear > self.front:
            self.front += 1
        else:
            print("队列为空")

    def enQueue(self, item):
        self.arr.append(item)
        self.rear += 1


class LNode():
    def __init__(self, x):
        self.data = x
        self.next = None


class Queue1():
    def __init__(self):
        self.phead = None
        self.pend = None

    def empty(self):
        if self.phead == self.pend:
            return True
        else:
            return False

    def size(self):
        size = 0
        p = self.phead
        while p != None:
            p = p.next
            size += 1
        return size

    def enQueue(self, e):
        '''
        入队列 把元素e加到队列尾
        :param e:
        :return:
        '''
        p = LNode()
        p.data = e
        p.next = None
        if self.phead is None:
            self.phead = self.pend = p
        else:
            self.pend.next = p
            self.pend = p

    def deQueue(self):
        '''
        出队列 删除队列首元素
        :return:
        '''
        if self.phead is None:
            print("出队失败 队列已为空")
        self.phead = self.phead.next
        if self.phead is None:
            self.pend = None

    def getFront(self):
        '''
        获取队首元素
        :return:
        '''
        if self.phead is None:
            return None
        return self.phead.data

    def getBack(self):
        if self.pend is None:
            return None
        return self.pend.data


