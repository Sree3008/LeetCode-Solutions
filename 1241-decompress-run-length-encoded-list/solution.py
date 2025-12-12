class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        for i in range(0,len(nums)):
            if i%2==0:
                list1.append(nums[i])
            else:
                list2.append(nums[i])
        list3=[]
        for i in range(len(list1)):
            list3.extend([list2[i]] * list1[i])
        return list3 


