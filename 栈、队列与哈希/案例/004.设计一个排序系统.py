from collections import deque


class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getSeq(self):
        return self.seq

    def setSeq(self, seq):
        self.seq = seq

    def equals(self, args0):
        o = args0
        return self.id == o.getId()


class Queue():
    def __init__(self):
        self.q = deque()

    def enQueue(self, u):
        '''
        进入队列的尾部
        :param u:
        :return:
        '''
        u.setSeq(len(self.q) + 1)
        self.q.append(u)

    def deQueue(self):
        '''
        出队列
        :return:
        '''
        self.q.popleft()
        self.updateSeq()

    def deQueuemove(self, u):
        self.q.remove(u)
        self.updateSeq()

    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    def printList(self):
        for u in self.q:
            print(u)
