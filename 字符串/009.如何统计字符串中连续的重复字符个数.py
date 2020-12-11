"""
递归实现一个求字符串中连续出现相同字符的最大值
例如 字符串 "aaabbcc" 最大值为a 3

解题思路
遍历字符串的时候定义两个变量 curMaxLen记录当前遍历字符重复的连续字符个数
maxLen遍历到目前为止找到最长的连续重复字符的个数
"""


def getMaxDupChar(s, startIndex, curMaxLen, maxLen):
    if startIndex == len(s) - 1:
        return max(curMaxLen, maxLen)
    if list(s)[startIndex] == list(s)[startIndex + 1]:
        return getMaxDupChar(s, startIndex + 1, curMaxLen + 1, maxLen)
    else:
        return getMaxDupChar(s, startIndex + 1, 1, max(curMaxLen, maxLen))


if __name__ == '__main__':
    s = getMaxDupChar('abbnnbc', 0, 1, 1)
    print(s)
