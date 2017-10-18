

def get_minimum_unique_sum(arr):

    # Check trivial cases
    if arr is None or (not isinstance(arr, list)) or len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    # First, sort the array
    arr = sorted(arr)

    # Then, loop through array and find duplicates. Once found, increment the integer by 1 until
    # a value that does not exist in the array is found.
    seen = []
    for i in range(0, len(arr)):
        if arr[i] not in seen:
            seen.append(arr[i])
        else:
            new_value = arr[i] + 1
            while True:
                if new_value not in arr:
                    break
                new_value += 1
            arr[i] = new_value

    return sum(arr)


if __name__ == '__main__':
    pass
