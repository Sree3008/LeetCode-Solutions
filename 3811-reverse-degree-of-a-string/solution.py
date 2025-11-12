class Solution:
    def reverseDegree(self, s: str) -> int:
        list=[]
        sum=0
        for i in s:
            b=ord(i)
            c=122-b+1
            list.append(c)
        for ind,val in enumerate(list):
            sum=sum+((ind+1)*val)
        return sum
