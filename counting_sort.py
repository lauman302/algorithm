def counting_sort(array):
    max_elem = max(array) + 1
    counted_values = [0] * max_elem
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(0, max_elem):
        for amount in range(0, counted_values[value]):
            array[index] = value
            index += 1 
    return array

nums = [5, 7, 1, 0, 1, 5, 11, 1]
counting_sort(nums)



def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)