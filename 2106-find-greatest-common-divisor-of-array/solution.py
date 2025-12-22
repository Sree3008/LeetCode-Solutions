class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        x=math.gcd(mini,maxi)
        return x
        
