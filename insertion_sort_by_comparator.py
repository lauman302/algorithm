def is_first_digit_weaker(digit_1, digit_2):
    return digit_1 < digit_2


def insertion_sort_by_comparator(array, length, less):
    for i in range(length-1):
        for j in range(0, length-i-1):
            var_1 = array[j] + array[j+1]
            var_2 = array[j+1] + array[j]
            if less(var_1, var_2):
                array[j], array[j+1] = array[j+1], array[j]
    print(*array, sep='')


if __name__ == '__main__':
    len_nums = int(input())
    numbers = input().split()
    insertion_sort_by_comparator(numbers, len_nums, is_first_digit_weaker)
