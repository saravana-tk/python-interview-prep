def selectionSort(nums):
    for ptr1 in range(len(nums) - 1):
        minindex = ptr1
        for ptr2 in range(ptr1 + 1, len(nums)):
            if nums[ptr2] < nums[minindex]:
                minindex = ptr2
        nums[ptr1], nums[minindex] = nums[minindex], nums[ptr1]
    return nums

print(selectionSort([6, 4, 2, -4, 8, -2, -1]))