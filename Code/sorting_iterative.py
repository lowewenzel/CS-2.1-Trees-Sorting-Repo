#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    length = len(items)
    for i in range(length - 1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if is_sorted(items):
        return True
    sorted = False
    while not sorted:
        swapped = False
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        if not swapped:
            sorted = True


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(len(items)):
        mindex = i

        for j in range(i + 1, len(items)):
            if items[j] < items[mindex]:
                mindex = j
        items[mindex], items[i] = items[i], items[mindex]
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    for i in range(1, len(items)):
        val = items[i]
        maxdex = i

        while maxdex and items[maxdex - 1] > val:
            items[maxdex] = items[maxdex - 1]
            maxdex = maxdex - 1
        items[maxdex] = val

    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
