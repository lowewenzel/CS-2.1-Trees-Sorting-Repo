#!python
from sorting_iterative import bubble_sort


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    if not items1 and not items2:
        return []

    result = []
    i, j = 0, 0
    length1, length2 = len(items1), len(items2)

    while (i < length1) and (j < length2):
        if items1[i] <= items2[j]:
            result.append(items1[i])
            i += 1
        else:
            result.append(items2[j])
            j += 1

    if i <= length1-1:
        while i < length1:
            result.append(items1[i])
            i += 1

    elif j <= length2-1:
        while j < length2:
            result.append(items2[j])
            j += 1

    return result


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order

    middle = len(items) // 2
    arr1, arr2 = items[0:middle], items[middle:]

    bubble_sort(arr1)
    bubble_sort(arr2)

    return merge(arr1, arr2)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) <= 1:
        return items  # base

    mid = len(items) // 2
    arr1, arr2 = items[0:mid], items[mid:]

    merge_sort(arr1)
    merge_sort(arr2)

    merged_items = merge(arr1, arr2)
    # copies the sorted part each time
    items[:] = merged_items
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot = items[high]  # just use the end

    cursor = low  # cursor is where the comparisons and swaps occur
    # O (range)
    for i in range(low, high):
        if items[i] <= pivot:
            items[i], items[cursor] = items[cursor], items[i]
            cursor += 1

    items[high], items[cursor] = items[cursor], items[high]

    return cursor


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low is None:
        low = 0
    if high is None:
        high = len(items) - 1

    if low <= high:
        # O (n)
        p = partition(items, low, high)
        # O (nlogn)
        quick_sort(items, low, p - 1)  # left sublist
        # O (nlogn)
        quick_sort(items, p + 1, high)  # right sublist


if __name__ == "__main__":
    arr = [33, 11, 84, 55, 77, 99, 40, 41, 42]
    print(arr)
    piv = partition(arr, 0, len(arr) - 1)
    print("pivot: ", arr[piv])
    print(arr)
