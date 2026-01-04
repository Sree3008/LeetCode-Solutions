class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=str(n)
        l1=list(s)
        list1=[]
        for i in range(len(l1)):
            if i%2==0:
                list1.append(int(l1[i]))
            else:
                list1.append(-(int(l1[i])))
        return sum(list1)
