class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        k=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                k=min(k,abs(start-i))
        return k
