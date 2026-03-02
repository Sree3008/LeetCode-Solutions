class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list1=[[]]
        for num in nums:
            for i in range(len(list1)):
                list1.append(list1[i]+[num])
        return list1
