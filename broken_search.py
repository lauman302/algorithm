def broken_search(nums, target) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        if nums[left] <= nums[middle]:
            if target < nums[middle] and target >= nums[left]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > nums[middle] and target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1
    return - 1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
