def bubblesort(arr):
    """
    Sort balabala

    :arr: unsorted list
    :return: sorted list
    """
    n = len(arr)

    # Outer loop
    for i in range(n - 1):

        # Inner loop
        for j in range(n - 1 - i):

            # Swap elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

return arr