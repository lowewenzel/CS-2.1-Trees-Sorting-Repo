#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    min_int = 0
    max_int = 0
    for val in numbers:
        if val >= max_int:
            max_int = val
        if val <= min_int:
            min_int = val

    counts = [None] * ((max_int+1) - min_int)

    for val in numbers:
        if counts[val] is not None:
            counts[val] += 1
        else:
            counts[val] = 1

    result = []
    for idx, val in enumerate(counts):
        if val is not None:
            result.extend([idx] * val)

    return result

    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


if __name__ == "__main__":
    arr = [6, 2, 8, 3, 2, 9, 2, 10, 5, 7, 1, 6]

    print(counting_sort(arr))
