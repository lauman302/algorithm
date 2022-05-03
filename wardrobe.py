def wardrobe(array, size, max_elem):
    max_elem = max_elem + 1
    counted_values = [0] * max_elem
    for value in array:
        counted_values[value] += 1
    
    index = 0
    for value in range(0, max_elem):
        for amount in range(0, counted_values[value]):
            array[index] = value
            index += 1
    return array



if __name__ == '__main__':
    count = int(input())
    if count:
        things = [int(num) for num in input().split()]
        print(*wardrobe(things, count, 2), sep=' ')