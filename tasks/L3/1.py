def removeElement(nums, val):
    k = 0  
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    return k



nums = [3, 2, 2, 3]
val = 3

print("Original array:", nums)
k = removeElement(nums, val)

print("k (number of elements not equal to val):", k)
print("Modified array:", nums[:k], end="")

print(" +", ["_"] * (len(nums) - k))
