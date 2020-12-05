"""
字母序列  [d,g,e,c,f,b,o,a]
实现一个方法 要求对方输入一组字符串 input= ['bed','dog','dear','eye'] 按照字母顺序排序并打印
dear dog eye bed

# 主要的思路
给定的字母序列建立一个可以进行大小比较的序列  采用map数据结构实现map的键为给定的字母序列 值为依次递增的正整数
对于没有在字母序列中的字母，对应的键按-1处理

"""


# 根据char_to_int规定的字符的大小关系比较两个字符的大小
def compare(str1, str2, char_to_int):
    len1 = len(str1)
    len2 = len(str2)
    i = 0
    j = 0
    while i < len1 and j < len2:
        if list(str1)[i] not in char_to_int.keys():
            char_to_int[list(str1)[i]] = -1

        if list(str2)[i] not in char_to_int.keys():
            char_to_int[list(str2)[j]] = -1
        # 比较各个字符的大小
        if char_to_int[list(str1)[i]] < char_to_int[list(str2)[j]]:
            return - 1

        elif char_to_int[list(str1)[i]] > char_to_int[list(str2)[j]]:
            return 1
        else:
            i += 1
            j += 1
    if i == len1 and j == len2:
        return 0
    elif i == len1:
        return -1
    else:
        return 1


def insertSort(s, char_to_int):
    lens = len(s)
    i = 1
    while i < lens:
        temp = s[i]
        j = i - 1
        while j >= 0:
            if compare(temp, s[j], char_to_int) == -1:
                s[j + 1] = s[j]
            else:
                break
            j -= 1
        s[j + 1] = temp
        i += 1


if __name__ == '__main__':
    s = ['bed', 'dog', 'dear', 'eye']
    seq = 'dgecfboa'
    lens = len(seq)
    char_to_int = dict()
    i = 0
    while i < lens:
        char_to_int[list(seq)[i]] = i
        i += 1
    insertSort(s, char_to_int)
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
