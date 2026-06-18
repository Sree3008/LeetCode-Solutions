class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        num1=nums[::-1]
        nums.extend(num1)
        return nums
