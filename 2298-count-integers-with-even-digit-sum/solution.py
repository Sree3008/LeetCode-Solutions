class Solution:
    def countEven(self, num: int) -> int:
        list1=[]
        for i in range(1,num+1):
            list1.append(str(i))
        c=0
        for i in list1:
            s=0
            for j in i:
                s=s+int(j)
            if s%2==0:
                c+=1
        return c
                





            
