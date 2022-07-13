
#Time O(nlogn)
def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]

#Time 0(log n)
def findMin(nums)->int:
    res=nums[0]
    l,r=0,len(nums)-1
    while l<=r:
        if nums[1]<nums[r]:
            res=min(res,nums[1])
            break
        m=(1+r)//2
        res=min(res,nums[m])
        if nums[m]>=nums[1]:
            l=m+1
        else:
            r=m-1