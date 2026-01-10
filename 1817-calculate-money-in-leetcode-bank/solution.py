class Solution:
    def totalMoney(self, n: int) -> int:
        list1=[]
        s=w=0
        while n>0:
            for j in range(1,8):
                if n==0:
                    break
                s+=j+w
                n-=1
            w+=1
        return s
