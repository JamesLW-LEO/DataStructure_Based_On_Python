"""
- 比较相邻的元素，如果第一个比第二个大，就交换它们两个
- 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
- 针对所有的元素重复以上的步骤，除了最后一个；
- 重复步骤1~3，直到排序完成。
"""


def bubbleSort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubbleSort1(arr):
    for i in range(len(arr) - 1, -1, -1):
        flag = 0  # 判断是否执行了交换操作
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag += 1
        if flag == 0:
            break
    return arr


if __name__ == '__main__':
    arr = [2, 14, 6, 4, 1, 5]
    res = bubbleSort1(arr)
    print(res)
