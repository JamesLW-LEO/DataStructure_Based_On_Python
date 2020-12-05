"""
字符串 "abcdfg"  "abdfg"
最长公共字串  "dfg"
"""


# 动态规划法
def getMaxSubStr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    maxL, count = 0, 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > maxL:
                    maxL = m[i + 1][j + 1]
                    count = i + 1
    return s1[count - maxL:count], maxL


print(getMaxSubStr('abcdfg', 'abdfg'))
