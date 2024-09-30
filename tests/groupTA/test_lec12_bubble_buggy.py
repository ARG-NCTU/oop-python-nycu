def bubble_sort(arr):
    """
    This function implements the bubble sort algorithm. Bubble sort is a simple sorting algorithm that repeatedly steps 
    through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list 
    is repeated until the list is sorted.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.
    """
    n = len(arr)  # Get the length of the list

    # Outer loop to iterate through each element in the list
    for i in range(n):

        # Inner loop to compare each element with the next one
        for j in range(n-1):

            # If the current element is greater than the next one, swap them
            if arr[j] > arr[j+1]:

                # swap arr[j] and arr[j+1] with temp variable
                temp = arr[j]  # Temporary variable to hold the current element
                arr[j] = arr[j+1]  # Replace current element with the next one
                arr[j+1] = temp  # Replace next element with the current one

    return arr  # Return the sorted list

print(bubble_sort([4, 2, 1, 8, 7, 6]))
