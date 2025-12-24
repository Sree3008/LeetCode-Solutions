class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if arr.count(i) > 1 and i == 0:
                return True 
            if i and i*2 in arr:
                return True
        return False
