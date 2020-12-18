def quickSort(arr):
    if len(arr) >= 2:
        mid = arr[len(arr) // 2]
        left, right = [], []
        arr.remove(mid)
        for i in arr:
            if i >= mid:
                right.append(i)
            else:
                left.append(i)
        return quickSort(left) + [mid] + quickSort(right)
    else:
        return arr


if __name__ == '__main__':
    res = quickSort([2, 45, 7, 234, 23, 66])
    print(res)
