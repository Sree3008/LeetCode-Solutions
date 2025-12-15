class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        x=Counter(nums)
        print(x)
        s=0
        for i,v in x.items():
            if v==1:
                s+=i
        return s
        

            
