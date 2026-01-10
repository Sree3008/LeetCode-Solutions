class Solution:
    def countBalls(self, l: int, h: int) -> int:
        list1=[]
        for i in range(l,h+1):
            s=0
            x=i
            while x>0:
                d=x%10
                s+=d
                x//=10
            list1.append(s) 
        z=Counter(list1)
        return max(z.values())

        
