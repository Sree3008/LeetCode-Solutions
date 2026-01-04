class Solution:
    def sumZero(self, n: int) -> List[int]:
        list1=[]
        if n % 2 != 0:
            list1.append(0)
        i=1
        while len(list1)<n:
            list1.append(i)
            list1.append(-i)
            i+=1
        return list1 
