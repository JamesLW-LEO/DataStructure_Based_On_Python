def getMaxProfit(l):
    # minPrice = float("inf") # 正负无穷 如果不好理解可以使用下边的方法
    minPrice = l[0]
    maxProfit = 0
    if len(l) <= 0:
        return
    for i in l[1:]:
        if i < minPrice:
            minPrice = i
        if i - minPrice > maxProfit:
            maxProfit = i - minPrice
    return maxProfit


if __name__ == '__main__':
    l = [7, 1, 5, 3, 6, 4]
    res = getMaxProfit(l)
    print(res)
