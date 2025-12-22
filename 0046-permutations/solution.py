class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p=permutations(nums)
        list1=[]
        for i in p:
            list1.append(i)
        return list1
        
