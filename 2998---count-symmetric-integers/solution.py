class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        list1=[]
        c=0
        for i in range(low,high+1):
            list1.append(str(i))
        for i in range(len(list1)):
            if len(list1[i])%2!=0:
                continue
            s=len(list1[i])//2
            l=sum(int(x) for x in list1[i][:s])
            r=sum(int(x) for x in list1[i][s:])
            if l==r:
                c+=1
        return c
        
