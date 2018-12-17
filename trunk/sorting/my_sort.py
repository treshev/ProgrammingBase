def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def bubble_sort(array):
    last_item = len(array) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(last_item):
            if array[i] > array[i + 1]:
                is_sorted = False
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
        last_item -= 1


def selection_sort(array):
    for start in range(len(array)):
        min_value = array[start]
        min_index = start
        for i in range(start, len(array)):
            if min_value >= array[i]:
                min_value = array[i]
                min_index = i

        if min_index != start:
            swap(array, start, min_index)


def insertion_sort(array):
    for i in range(1, len(array)):
        current = i
        while current > 0 and array[current] < array[current - 1]:
            swap(array, current, current - 1)
            current -= 1


def merge(array: list, start, end):
    median = start + int((end - start) / 2)
    tmp = []
    leftStart = start
    rightStart = median + 1
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


def merge_sorting(array, start, end):
    if start < end:
        medium = start + int((end - start) / 2)
        merge_sorting(array, start, medium)
        merge_sorting(array, medium + 1, end)
        merge(array, start, end)


def merge_sort(array):
    merge_sorting(array, 0, len(array) - 1)
