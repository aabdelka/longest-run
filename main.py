"""
Assumes L is a list of integers containing at least 2 elements.
Finds the longest run of numbers in L, where the longest run can
either be monotonically increasing or monotonically decreasing.
In case of a tie for the longest run, choose the longest run
that occurs first.
Does not modify the list.
Returns the sum of the longest run.
"""


def longest_run(arr):
    array = arr[:]

    # Not required since arr's length is assumed to be at least 2
    # if len(array) < 2:
    #     return None

    # Return the sum of arr if length equals 2
    if len(array) == 2:
        return sum(array)

    # The approach in solving the problem is break the list in to
    # sub-list of monotonically increasing/decreasing integers
    mono_arrays = []

    # Initialise the previous value
    previous = array[0]
    # Current found monotonic list
    current_mono = [previous]

    # Flag to toggle between checking increasing/decreasing integers
    toggle_check = True

    # TODO: Make the code DRY
    for num in array[1:]:
        if toggle_check:
            if previous < num:
                current_mono.append(num)
                previous = num
            else:
                toggle_check = False
                mono_arrays.append(current_mono[:])
                # previous = num
                current_mono.clear()
                current_mono.append(previous)
        if not toggle_check:
            if previous > num:
                current_mono.append(num)
                previous = num
            else:
                toggle_check = True
                mono_arrays.append(current_mono[:])
                current_mono.clear()
                current_mono.append(previous)
                current_mono.append(num)
                previous = num

    mono_arrays.append(current_mono[:])

    # Calculate the length of all monotonic sub-lists
    array_lengths = [len(array) for array in mono_arrays]
    # Find the list with the max length. Get its position in the list.
    # Use the index to retrieve the corresponding sub-list and return its sum
    return sum(mono_arrays[array_lengths.index(max(array_lengths))])
