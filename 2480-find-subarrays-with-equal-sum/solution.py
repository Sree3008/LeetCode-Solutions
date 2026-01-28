class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        list2=set()
        for i in range(len(nums)-1):
            x=nums[i+1]+nums[i]
            if x in list2:
                return True
            list2.add(x)
        return False


            
