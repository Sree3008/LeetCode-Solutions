class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for i,v in x.items():
            if v%2!=0:
                return False
        return True
