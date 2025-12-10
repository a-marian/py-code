def bubble_sort(arr):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Bubble sort repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. This process is repeated
    until the list is sorted.

    :param arr: The list of elements to sort.
    :type arr: list of int or float
    :returns: The sorted list in ascending order. The sorting is performed in-place,
              but the same list is also returned for convenience.
    :rtype: list of int or float
    :raises TypeError: If the input is not a list, or if the list contains elements that cannot be compared.

    Example::

        >>> bubble_sort([3, 1, 4, 2])
        [1, 2, 3, 4]

    .. note::
        This implementation has a time complexity of O(n^2) and is not suitable for large lists.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr