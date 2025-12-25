class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        list1=[]
        c=0
        for i in arr1:
            b=True
            for j in arr2:
                if abs(i-j)<=d:
                    b=False
                    break
            if b:
                c+=1
        return c
