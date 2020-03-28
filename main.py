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

    if len(array) < 2:
        return None
    if len(array) == 2:
        return sum(array)

    mono_arrays = []

    previous = array[0]
    current_mono = [previous]
    toggle_check = True

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
    # print(mono_arrays)

    array_lengths = [len(array) for array in mono_arrays]
    # print(array_lengths)
    return sum(mono_arrays[array_lengths.index(max(array_lengths))])
