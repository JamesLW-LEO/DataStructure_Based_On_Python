def build_heap(arr, size):
    """
    构造一个堆，将堆中所有数据重新排序
    :param arr:
    :param size:
    :return:
    """
    for i in range(0, size // 2)[::-1]:
        ad_heap(arr, i, size)


def ad_heap(arr, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    maxs = i
    if i < size // 2:
        if lchild < size and arr[lchild] > arr[maxs]:
            maxs = lchild
        if rchild < size and arr[rchild] > arr[maxs]:
            maxs = rchild
        if maxs != i:
            arr[maxs], arr[i] = arr[i], arr[maxs]
            ad_heap(arr, maxs, size)


def heapSort(arr, size):
    # 将根节点取出与最后一位做对调，对前面len :- 1个节点继续进行堆调整过程。
    build_heap(arr, size)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(0, size)[::-1]:
        arr[0], arr[i] = arr[i], arr[0]
        ad_heap(arr, 0, i)


if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    heapSort(a, len(a))
    print(a)
