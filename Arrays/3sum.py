

def threeSum(nums):
    l = 0
    r = len(nums)-1
    target = 0
    triplets = []
    nums.sort()
    if nums == [] or nums == [0]:
            return []

    for i in range(len(nums)-1):
        l = i+1
        r = len(nums)-1
        while (l < r):
            total = nums[i] + nums[l] + nums[r]
            if total == target:
                val = [nums[i], nums[l], nums[r]]
                if val not in triplets:
                    triplets.append(val)
                l += 1
                r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
    print(triplets)
    return triplets


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
