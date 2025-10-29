
nums = [2, 7, 11, 15]
target = 9
hashmap = {}
for index, num in enumerate(nums):
    complement = target - num
    if complement in hashmap:
        print("Indices:", [hashmap[complement], index])
        print("Numbers:", [nums[hashmap[complement]], nums[index]])
        break
    hashmap[num] = index
