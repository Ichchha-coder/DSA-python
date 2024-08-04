def selection_sort(arr):
    n = arr.length
    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_idx = i
        for j in range(i + 1, n):
            # Update min_idx if the element at j is smaller than the current minimum
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr