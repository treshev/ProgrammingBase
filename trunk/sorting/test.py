def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def insertion_sort(array):
    result = 0
    for i in range(1, len(array)):
        current = i
        while current > 0 and array[current] < array[current - 1]:
            swap(array, current, current - 1)
            result += 1
            current -= 1
    print("Insert", result)


def merge(array: list, start, end):
    med = int((end - start) / 2)
    median = start + med
    tmp = []
    leftStart = start
    rightStart = median + 1
    result = 0
    second_part = array[median + 1: end + 1]
    while leftStart <= median and rightStart <= end:
        if array[leftStart] < array[rightStart]:
            tmp.append(array[leftStart])
            leftStart += 1
        else:
            tmp.append(array[rightStart])
            rightStart += 1

    while rightStart <= end:
        tmp.append(array[rightStart])
        rightStart += 1

    while leftStart <= median:
        tmp.append(array[leftStart])
        leftStart += 1

    for i in range(len(tmp)):
        array[start + i] = tmp[i]

    for i in range(len(second_part)):
        if second_part[i]!=tmp[med+1+i]:
            result += i - tmp.index(second_part[i])

    return result if result > 0 else 0


def merge_sorting(array, start, end, result):
    if start < end:
        medium = start + int((end - start) / 2)
        merge_sorting(array, start, medium, result)
        merge_sorting(array, medium + 1, end, result)
        result[0] += merge(array, start, end)
    return result[0]


def merge_sort(array):
    print("Merge", merge_sorting(array, 0, len(array) - 1, [0]))


if __name__ == '__main__':
    # with open("input.txt") as input:
    #     N = int(input.readline())
    #     for _ in range(N):
    #         input.readline()
    #         text_array = input.readline().strip().split()
    #         array = list(map(int, text_array))
    #         merge_sort(array)
    #         # print(len(array), array[0], array[-1])

    # a = [10, 9, 2, 3, 4, 5, 6, 7, 8, 0]
    a = [7,8,9,0,1]
    b = a[:]
    merge_sort(a)
    insertion_sort(b)
