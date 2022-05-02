def insertion_sort(array):
    ''' Function to do insertion sort values'''
    # Traverse throug 1 to len(array)
    for i in range(1, len(array)):
        item_to_insert = array[i]
        # move elements of array[0, i-1], that are
        # grater than item_to_insert, to one position ahead
        # of their current position
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')
    print(array)


insertion_sort([11, 2, 9, 7, 1])
