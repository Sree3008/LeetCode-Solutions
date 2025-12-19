class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        x=Counter(nums)
        print(x)
        s=0
        for i,v in x.items():
            if v%k==0:
                y=i*v
                s+=y
        return s
