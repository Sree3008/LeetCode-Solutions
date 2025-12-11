class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        s=str(num)
        list1=[]
        for i in s:
            list1.append(int(i))
        for i in list1:
            if num%i==0:
                c+=1
        return c
            
