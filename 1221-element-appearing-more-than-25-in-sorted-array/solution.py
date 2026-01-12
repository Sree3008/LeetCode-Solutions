class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l=len(arr)
        for i in range(l):
            if arr[i]==arr[i+l//4]:
                return arr[i]
        
        
