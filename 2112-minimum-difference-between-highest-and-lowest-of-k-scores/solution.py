class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        list2=[]
        for i in range(len(nums)-k+1):
            list1=[]
            for j in range(i,i+k):
                    list1.append(nums[j])
            list2.append(list1)
        list3=[]
        for i in list2:
            x=min(i)
            y=max(i)
            list3.append(y-x)
        return min(list3)
            
        
