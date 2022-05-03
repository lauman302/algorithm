def letter_combinations(digits):
    letters = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        for letter in letters[digits[0]]:
            path += letter
            backtrack(digits[1:], path, res)
            path = path[:-1]
    res = []
    backtrack(digits, '', res)
    return res


if __name__ == '__main__':
    digits = input()
    print(*letter_combinations(digits), end=' ')



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