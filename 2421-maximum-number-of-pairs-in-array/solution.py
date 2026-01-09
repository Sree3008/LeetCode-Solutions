class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        list1=[]
        x=Counter(nums)
        res1=0
        res2=0
        for i in x.values():
            res1+=i//2
            res2+=i%2
        return [res1,res2] 
        
