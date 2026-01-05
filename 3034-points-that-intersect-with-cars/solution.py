class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        list1=set()
        for i in nums:
            for j in range(i[0],i[1]+1):
                list1.add(j)
        return len(list1)
        
