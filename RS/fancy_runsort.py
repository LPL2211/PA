import sys


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


def find_run_reverse(arr, start):
    """
    Looks for decreasing runs
    """
    l = len(arr)

    if start is None:
        return None

    if start >= l:
        return None

    prev = arr[start]
    while(start < l):
        if prev < arr[start]:
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


def fancy_runsort(arr):
    """
    Optimized runsort
    """
    i = 0

    if not is_sorted(arr):
        while i is not None:
            first_run_end = find_run(arr, i)

            # if the length of non-decreasing run is 1, look for decreasing runs
            # and then reverse them
            if first_run_end and first_run_end == i + 1:
                first_run_end = find_run_reverse(arr, i)
                # pythonic way of reversing a slice of an array
                arr[i: first_run_end] = arr[i: first_run_end][::-1]

            second_run_end = find_run(arr, first_run_end)

            # mirror down run for second array
            if second_run_end and second_run_end == first_run_end + 1:
                second_run_end = find_run_reverse(arr, first_run_end)
                arr[first_run_end: second_run_end] = arr[first_run_end: second_run_end][::-1]

            if second_run_end:

                left = arr[i: first_run_end]
                right = arr[first_run_end: second_run_end]
                left_run_size = len(left)
                right_run_size = len(right)

                if left_run_size > 8 and right_run_size > 8:
                    arr[i: second_run_end] = merge(left + right,
                                                   left,
                                                   right)
                else:
                    # insertion sort for run sizes less than 8
                    arr[i:second_run_end] = insertion_sort(left + right)

            i = second_run_end

        fancy_runsort(arr)


def insertion_sort(arr):
    for index in range(1, len(arr)):

        c_val = arr[index]
        pos = index

        while pos > 0 and arr[pos - 1] > c_val:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = c_val

    return arr


data = sys.stdin.readlines()

# data = []

# with open("input.txt", "r") as f:
#     data = f.readlines()

data = [e.strip() for e in data]
fancy_runsort(data)

for e in data:
    print(e)
