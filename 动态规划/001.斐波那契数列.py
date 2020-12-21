# 相当于函数缓冲
# 加递归调用
# 为了避免重复
# 可以把计算过的值存起来
# 当再次用到时
# 可以直接使用
# 这其实是用空间换时间


def fib(x):
    d = {}
    for i in range(x + 1):
        if i < 2:
            f = i
        else:
            f = d[i - 1] + d[i - 2]
        d[i] = f
    return d


if __name__ == '__main__':
    res = fib(4)
    print(res)
