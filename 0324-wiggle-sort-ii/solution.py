class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        x=(len(nums)+1)//2
        list1=nums[:x][::-1]
        list2=nums[x:][::-1]
        nums.clear()
        for i in range(len(list2)):
            nums.append(list1[i])
            nums.append(list2[i]) 
        if len(list1) > len(list2):
            nums.append(list1[-1])
        
