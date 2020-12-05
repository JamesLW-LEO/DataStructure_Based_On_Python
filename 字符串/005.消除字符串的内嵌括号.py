"""
给定一个如下格式的字符串，(1,(2,3),(4,(5,6),7)) 括号内的元素可以是数字 也可以是另外一个括号
实现一个算法消除嵌套括号 例如变成(1,2,3,4,5,6,7) 如果表达式有误 就报错
"""


def removeNestedOare(strs):
    if strs == None:
        return strs
    Parentheses_num = 0  # 用来记录不匹配的 ‘(’出现的次数
    if list(strs)[0] != '(' or list(strs)[-1] != ')':
        return None
    sb = '('
    # 字符串首尾的括号可以单独处理
    i = 1
    while i < len(strs) - 1:
        ch = list(strs)[i]
        if ch == "(":
            Parentheses_num += 1
        elif ch == ')':
            Parentheses_num -= 1
        else:
            sb = sb + (list(strs)[i])
        i += 1
    # 判断括号是否匹配
    if Parentheses_num != 0:
        print("括号不匹配")
        return None
    sb = sb + ')'
    return sb


strs = '(1, (2, 3), (4, (5, 6), 7))'
res = removeNestedOare(strs)
print(res)
