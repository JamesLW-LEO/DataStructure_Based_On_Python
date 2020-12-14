def shellSort(arr):
    k = 1
    jmp = len(arr) // 2
    while jmp != 0:
        for i in range(jmp, len(arr)):
            tmp = arr[i]
            j = i - jmp
            while tmp < arr[j] and j >= 0:
                arr[j + jmp] = arr[j]
                j = j - jmp
            arr[jmp + j] = tmp
        print("第{0}次排序过程".format(k))
        k += 1
        jmp = jmp // 2
    return arr


if __name__ == '__main__':
    arr = [2, 14, 6, 4, 1, 5]
    res = shellSort(arr)
    print(res)
