class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=str(nums)
        print(s)
        x=0
        for i in s:
            if i=='[' or i==']' or i==',' or i==' ':
                continue
            else:
                x=x+int(i)
        y=sum(nums)
        return abs(y-x)
