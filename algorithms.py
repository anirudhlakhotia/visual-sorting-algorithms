def bubble_sort(array):
    n = len(array)
    for i in range(n):
        """Check if its already sorted
        already_sorted = True"""

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                """If the item you're looking at is greater than its
                adjacent value, then swap them"""
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                """already_sorted = False"""

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        """if already_sorted:
            break"""

    return array


def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array


def merge_sort(A, start, end):
    """Merge sort."""

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    merge_sort(A, start, mid)
    merge_sort(A, mid + 1, end)
    merge(A, start, mid, end)
    return A


def merge(A, start, mid, end):
    """Helper function for merge sort."""

    merged = []
    left_index = start
    right_index = mid + 1

    while left_index <= mid and right_index <= end:
        if A[left_index] < A[right_index]:
            merged.append(A[left_index])
            left_index += 1
        else:
            merged.append(A[right_index])
            right_index += 1

    while left_index <= mid:
        merged.append(A[left_index])
        left_index += 1

    while right_index <= end:
        merged.append(A[right_index])
        right_index += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val


def quick_sort(array, start, end):
    """In-place Quick Sort."""

    if start >= end:
        return

    pivot = array[end]
    pivot_index = start

    for i in range(start, end):
        if array[i] < pivot:
            array[i], array[pivot_index] = array[pivot_index], array[i]
            pivot_index += 1
    array[end], array[pivot_index] = array[pivot_index], array[end]

    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)
    return array


def count_sort(array):
    """Count Sort."""

    # Trying my own implementation(should be same time complexity O(m+2*n))
    count = [0] * (max(array) + 1)
    for i in range(0, len(array)):
        count[array[i]] += 1
    j = 0
    for i in range(0, len(count)):
        for k in range(0, count[i]):
            array[j] = i
            j += 1

    return array
