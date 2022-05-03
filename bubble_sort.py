def bubble_sort(digits, length):
    flag = 1
    for i in range(length):
        for j in range(0, length - i - 1):
            if digits[j] > digits[j + 1]:
                digits[j], digits[j + 1] = digits[j + 1], digits[j]
                flag = 1
        if flag == 1:
            print(*digits)
            flag = 0


if __name__ == '__main__':
    length = int(input())
    digits = [int(digit) for digit in input().split()]
    bubble_sort(digits, length)