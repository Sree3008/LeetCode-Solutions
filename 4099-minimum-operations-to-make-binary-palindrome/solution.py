class Solution:
    def is_bin(self,x):
        b=bin(x)[2:]
        return b==b[::-1]
    def minOperations(self, nums: List[int]) -> List[int]:
        ans=[]
        for x in nums:
            if self.is_bin(x):
                ans.append(0)
                continue
            steps=1
            while True:
                if x-steps>0 and self.is_bin(x-steps):
                    ans.append(steps)
                    break
                if self.is_bin(x+steps): 
                    ans.append(steps)
                    break
                steps+=1
        return ans
                
