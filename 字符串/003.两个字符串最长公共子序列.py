"""
给定两个字符串A，B，长度分别为m，n。要求求出他们的最长公共子序列，返回其长度，例如
    A = "hello word"
    B = "loop"
最长公共子序列为“loo” 长度为3
# 思路
动态规划的子问题res[i][j]为截止到字符串A的第i个字符和截止到字符串B的第j个字符的最长公共子序列。由此可以得出递推公式
当i=0 or j=0  res[i][j] = 0
当A[i] == B[j]时 res[i][j] = res[i-1][j-1]+1
当A[i]!=B[j]时 res[i][j] = max(res[i-1][j],res[i][j+1])

"""


def LCS(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
            else:
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
    return res, res[-1][-1]


print(LCS("helloworld", "loop"))
