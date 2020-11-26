"""
LRU
最近最少使用
缓冲一定量的数据 当超过设定的阈值时 就把过期数据删除

# 实现方式
    使用双向链表实现的队列 队列的最大容量为缓冲的大小 在使用过程中 把最近使用的页面移动到队列头 最近未使用的放队尾
    使用一个哈希表 把页号作为键  把缓冲在队列中的节点的地址作为值
"""

from collections import deque


class LRU():
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.queue = deque()
        self.hashSet = set()

    def isQueueFull(self):
        '''
        判断缓冲队列是否已满
        :return:
        '''
        return len(self.queue) == self.cacheSize

    def enqueue(self, pageNum):
        '''
        把页号为pageNum的页缓冲到队列 同时添加到hash表中
        :param pageNum:
        :return:
        '''
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        # 把新缓冲的节点同时添加到hash表中
        self.hashSet.add(pageNum)

    def accessPage(self, pageNum):
        if pageNum not in self.hashSet:
            self.enqueue(pageNum)
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())


if __name__ == '__main__':
    l = LRU(3)
    l.accessPage(1)
    l.accessPage(3)
    l.accessPage(4)
    l.accessPage(1)
    l.accessPage(6)
    l.accessPage(9)
    l.printQueue()
    print(l.hashSet)
