class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        list1=[]
        res=n//3
        x=Counter(nums)
        for i,v in x.items():
            if v>res:
                list1.append(i)
        return list1
