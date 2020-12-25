def djjs(arr):
    res_list = []
    temp = 0
    for i in range(0, len(arr), 2):
        temp += arr[i]
        res_list.append(temp)
    maxs = max(res_list)
    return maxs


if __name__ == '__main__':
    arr = [2, 4, 2, 9, 12, 1]
    res = djjs(arr)
    print(res)
