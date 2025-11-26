def count_swaps(original, target):
    index_map = {v: i for i, v in enumerate(original)}
    swaps = 0
    arr = original[:]

    for i in range(len(arr)):
        correct_value = target[i]

        if arr[i] != correct_value:
            swaps += 1

            # swap current with the location of the correct value
            swap_idx = index_map[correct_value]

            # update map before swapping
            index_map[arr[i]] = swap_idx
            index_map[correct_value] = i

            arr[i], arr[swap_idx] = arr[swap_idx], arr[i]

    return swaps


def lilysHomework(arr):
    asc = sorted(arr)
    desc = asc[::-1]

    return min(count_swaps(arr, asc), count_swaps(arr, desc))


 
n = int(input().strip())
arr = list(map(int, input().split()))
print(lilysHomework(arr))
