class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        list1=[]
        for i in range(1,n+1):
            if n%i==0:
                list1.append(i)
        if len(list1)>=k:
            return list1[k-1]
        return -1

