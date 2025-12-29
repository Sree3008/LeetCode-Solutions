class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        list1=[]
        list2=[]
        for i in range(1,n+1):
            if i%m==0:
                list1.append(i)
            else:
                list2.append(i)
        return -(sum(list1)-sum(list2))

