from typing import List

arr = [8, 2, 10, 15, 21, 26]

# пузырьковая сортировка
def bubble_sort(arr: List[int]) -> List[int]:
    def swap(left: int, right: int) -> None:
        arr[left], arr[right] = arr[right], arr[left]

    count: int = len(arr)
    swapped: bool = True
    x: int = -1

    while swapped:
        swapped: bool = False
#        x += 1 # 0
        for i in range(1, count):
            if arr[i-1] > arr[i]:
                swap(i-1, i)
                swapped = True
    return arr

print(bubble_sort(arr))

# сортировка выбором

def selection_sort(arr: List[int]) -> List[int]:
    for ext_i in range(len(arr)):
        minimum: int = ext_i
        for int_i in range(ext_i + 1, len(arr)):
            if arr[int_i] < arr[ext_i]:
                minimum = int_i
        arr[ext_i], arr[minimum] = arr[minimum], arr[ext_i]
    return arr

print(selection_sort(arr))

# Ближайший ноль

n = 5
arr = [0, 1, 4, 9, 0]

def nearest_zero(distance):
    zeros = [0] * len(distance)
    print(zeros)
    index_zeros = [i for i in range(len(distance)) if distance[i] == 0]
    print(index_zeros)
    for i in range(index_zeros[0], len(distance), +1):
        print(index_zeros[0], len(distance))
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = zeros[i-1] + 1
    for i in range(index_zeros[-1], index_zeros[0], -1):
        if distance[i] == 0:
            zeros[i] = 0
        else:
            zeros[i] = min(zeros[i], zeros[i + 1] + 1)
    for i in range(index_zeros[0] - 1, -1, -1):
        zeros[i] = zeros[i + 1] + 1
    return zeros

distance = [0, 1 , 4, 9, 0]
print(nearest_zero(distance))

for i in range(0, 5, +1):
    print(i)