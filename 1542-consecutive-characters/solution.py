class Solution:
    def maxPower(self, s: str) -> int:
        list1=list(s)
        maxi=0
        c=0
        for i in range(1,len(list1)):
            if list1[i]==list1[i-1]:
                c+=1
            else:
                if maxi<c:
                    maxi=c
                c=0
        if maxi<c:
            maxi=c
        return maxi+1

        
        
