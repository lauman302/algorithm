def letter_combinations(nums, left, right, prefix):
    if left == 0 and right == 0:
        print(prefix)
    else:
        left > 


if __name__ == '__main__':
    letters = {
        2: 'abc', 3: 'def',
        4: 'ghi', 5: 'jkl',
        6: 'mno', 7: 'pqrs',
        8: 'tuv', 9: 'wxyz'
    }
    nums = [num for num in input().split()]
    cnt = 0
    left = letters[nums[0]]
    right = letters[nums[1]]
    letter_combinations(nums, left, right, '')
