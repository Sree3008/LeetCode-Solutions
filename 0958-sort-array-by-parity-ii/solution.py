class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        list1=[]
        list2=[]
        for i in nums:
            if i%2==0:
                list1.append(i)
            else:
                list2.append(i)
        print(list1)
        print(list2)
        list3=[]
        for i in range(0,len(nums)//2):
            list3.append(list1[i])
            list3.append(list2[i])
        return list3
