class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        list1=[]
        for i in nums:
            x=str(i)
            list1.append(int(x[::-1]))
        nums.extend(list1)
        return len(set(nums))

