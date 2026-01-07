class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        list1=[]
        for i in range(len(s)):
            x=abs(i-t.index(s[i]))
            list1.append(x)
        return sum(list1) 

            

            
            

        
