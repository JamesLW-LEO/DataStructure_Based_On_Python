"""
回文字符串：一个字符串从左到右与从右到左遍历得到的序列是相同的
例如 abcaba是回文字符串  abcab不是回文字符串
"""


# 动态规划法

class Test():
    def __init__(self):
        """
        分别表示 找到回文字符串的起始位置 和 长度
        """
        self.startIndex = None
        self.lens = None

    def getStartIndex(self):
        return self.startIndex

    def getLens(self):
        return self.lens

    def getLongestPalindrome(self, strs):
        if strs == None:
            return
        n = len(strs)
        if n < 1:
            return
        self.startIndex = 0
        self.lens = 1
        # 申请额外的存储空间记录查找的历史信息
        historyRecord = [([0] * n) for i in range(n)]
        print(historyRecord)
        # i = 0
        # while i < n:
        #     j = 0
        #     while j < n:
        #         historyRecord[i][j] = 0
        #         j += 1
        #     i += 1
        # 初始化长度为1的回文字符串的信息
        i = 0
        while i < n:
            historyRecord[i][i] = 1
            i += 1
        print(historyRecord)
        # 初始化长度为2的回文字符串的信息
        i = 0
        while i < n - 1:
            if list(strs)[i] == list(strs)[i + 1]:
                historyRecord[i][i + 1] = 1
                self.startIndex = i
                self.lens = 2
            i += 1
        print(historyRecord)
        plen = 3
        while plen < n:
            i = 0
            while i < n - plen + 1:
                j = i + plen - 1
                if list(strs)[i] == list(strs)[j] and historyRecord[i + 1][j - 1]:
                    historyRecord[i][j] = 1
                    self.startIndex = i
                    self.lens = plen
                i += 1
            plen += 1

        print(historyRecord)


import numpy as np


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        # 保存状态的矩阵
        matrix = np.zeros((len(s), len(s)), dtype=bool)
        max_len = 0  # 最长回文字符串的大小
        loc = (0, 0)  # start,end 最长回文串的位置
        # 动态规划求解
        for j in range(0, len(s)):
            for i in range(0, j + 1):
                if s[i] == s[j] and (j - i < 2 or matrix[i + 1][j - 1]):
                    matrix[i][j] = True
                    if max_len < j - i + 1:
                        max_len = j - i + 1  # 长度
                        loc = (i, j)  # 位置

        return s[loc[0]:loc[0] + max_len]


if __name__ == '__main__':
    strs = 'abcdefgfedxyz'
    t = Test()
    t.getLongestPalindrome(strs)
    if t.getStartIndex() != -1 and t.getLens() != -1:
        i = t.getStartIndex()
        while i < t.getStartIndex() + t.getLens():
            print(list(strs)[i], end='')
            i += 1
    s = Solution()
    res = s.longestPalindrome("ababe")
    print(res)
