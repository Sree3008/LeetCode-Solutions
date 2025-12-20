class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        list1=[nums[i] for i in range(n)]
        list2=[nums[i] for i in range(n,len(nums))]
        list3=[]
        for i in range(n):
            list3.append(list1[i])
            list3.append(list2[i])
        return list3
        
