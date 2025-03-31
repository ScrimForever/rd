def bin_search(list, target):
    list.sort() # It´s not necessary really, but it´s a good practice to sort the list before binary search
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2

        if list[mid] == target:
            return mid
        if list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

