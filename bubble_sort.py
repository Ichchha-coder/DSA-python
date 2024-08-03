def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Initialize a flag to detect any swap
        swapped = False
        
        # Traverse the array from 0 to n-i-1
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no elements were swapped, break the loop
        if not swapped:
            break
    return arr