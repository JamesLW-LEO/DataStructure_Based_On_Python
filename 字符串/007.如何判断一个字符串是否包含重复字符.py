"""
判断一个字符串是否重复字符 例如：good就包含重复字符 而abc就不包含重复字符串

"""


def isDup(strs):
    lens = len(strs)
    i = 0
    while i < lens:
        j = i + 1
        while j < lens:
            if list(strs)[j] == list(strs)[i]:
                return True
            j += 1
        i += 1
    return False


if __name__ == '__main__':
    strs = 'abcdefghijk'
    res = isDup(strs)
    print(res)
