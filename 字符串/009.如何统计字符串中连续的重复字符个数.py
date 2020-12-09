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


def func(s):
    maxLen = 0
    curLen = 1
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            curLen += 1
        else:
            maxLen = curLen
    return max(curLen, maxLen)


if __name__ == '__main__':
    s = getMaxDupChar('abbabc', 0, 1, 1)
    print(func('abbnbc'))
    print(s)
