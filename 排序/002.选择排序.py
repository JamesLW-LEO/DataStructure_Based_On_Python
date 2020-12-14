def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    return arr


if __name__ == '__main__':
    arr = [2, 14, 6, 4, 1, 5]
    res = selectionSort(arr)
    print(res)
    import os

    print(os.path.abspath("\\JavaProject"))
