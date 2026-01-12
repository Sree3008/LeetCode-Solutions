class Solution:
    def maximumUnits(self, nums: List[List[int]], n: int) -> int:
        list1=[]
        nums.sort(key=lambda x: x[1], reverse=True)
        for i in nums:
            if n==0:
                break
            z=min(i[0],n)
            list1.append(z*i[1]) 
            n-=z 
        return sum(list1)
        
        
