def mergeSort(arr):
    lens = len(arr)
    if lens < 2:
        return arr
    middle = lens // 2
    left = arr[: middle]
    right = arr[middle:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    c = []
    h, j = 0, 0
    while j < len(left) and h < len(right):
        if left[j] < right[h]:
            c.append(left[j])
            j += 1
        else:
            c.append(right[h])
            h += 1

    if j == len(left):
        for i in right[h:]:
            c.append(i)
    else:
        for i in left[j:]:
            c.append(i)

    return c


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(mergeSort(a))



