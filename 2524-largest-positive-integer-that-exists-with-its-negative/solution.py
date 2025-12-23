class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        p=[]
        n=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        p.sort()
        p.reverse()
        for i in p:
            if -i in n:
                return i
        return -1

