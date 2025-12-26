class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        x=Counter(nums)
        for i,v in x.items():
            c=0
            for j in range(1,v+1):
                if v%j==0:
                    c+=1
            if c==2:
                return True
        return False

