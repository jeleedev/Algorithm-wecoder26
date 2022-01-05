def selectionSort(nums):
    for i in range(0, len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

nums = [4, 9, 11, 14]
target = 13

print("nums: ", selectionSort(nums))