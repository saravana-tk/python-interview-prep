def selectionSort(nums):
    for i in range(len(nums) - 1):
        min = nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(selectionSort([6, 4, 9, 7, 8, 0, -1]))