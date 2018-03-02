import sys


def runsort(arr):
    """
    Sorts an array.
    """
    i = 0

    if not is_sorted(arr):
        while i is not None:
            first_run_end = find_run(arr, i)
            second_run_end = find_run(arr, first_run_end)

            if second_run_end:
                left = arr[i: first_run_end]
                right = arr[first_run_end: second_run_end]
                arr[i: second_run_end] = merge(arr[i: second_run_end],
                                               left,
                                               right)

            i = second_run_end

        runsort(arr)


def merge(arr, left, right):
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

        return arr


def find_run(arr, start):
    """
    Returns the end slice index of the run in the arr
    starting from index "start"
    """
    l = len(arr)

    if start is None:
        return None

    if start >= l:
        return None

    prev = arr[start]
    while(start < l):
        if prev > arr[start]:
            break
        prev = arr[start]
        start += 1

    return start


def is_sorted(arr):
    res = True

    prev = arr[0]
    for e in arr:
        if e < prev:
            res = False
            break
        prev = e

    return res


data = sys.stdin.readlines()

# data = []

# with open("input.txt", "r") as f:
#     data = f.readlines()

data = [e.strip() for e in data]
runsort(data)

for e in data:
    print(e)
