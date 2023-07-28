def find_uniq(arr):
    return set(arr[:len(arr)//2]).symmetric_difference(set(arr[len(arr)//2:])).pop()