class Solution:
    def slowestKey(self, nums: List[int], keys: str) -> str:
        list1=[]
        list1.append(nums[0])
        for i in range(1,len(nums)):
            x=nums[i]-nums[i-1]
            list1.append(x)
        list2=[]
        for i in zip(list1,keys):
            list2.append(i)
        list2.sort()
        return list2[-1][1]

        
