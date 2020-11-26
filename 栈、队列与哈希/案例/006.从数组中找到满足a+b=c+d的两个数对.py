"""
描述 给定一个数组 在数组中找出两个数对 满足 a+b = c+d

解题思路
以数对为单位进行遍历 在遍历过程中 把数对和数对的值存储在字典中 键位数对的和 值为数对
当遍历到一个键值对时  如果它的和在字典中已经存在 那么就满足条件

"""


class pair():
    def __init__(self, first, second):
        self.first = first
        self.second = second


def findPairs(arr):
    # 键为数对的和 值为数对
    sumPair = {}
    n = len(arr)
    # 遍历数组中所有可能的数对
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            sums = arr[i] + arr[j]
            if sums not in sumPair:
                sumPair[sums] = pair(i, j)
            else:
                p = sumPair[sums]
                print(arr[p.first], arr[p.second], arr[i], arr[j])
            j += 1
        i += 1
    print(sumPair)


if __name__ == '__main__':
    arr = [3, 4, 7, 10, 20, 9, 8]
    findPairs(arr)
