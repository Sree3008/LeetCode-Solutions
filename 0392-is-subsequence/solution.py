class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        list1=[]
        for i in s:
            list1.append(i)
        k=0
        for i in t:
            if k<len(list1) and i==list1[k]: 
                k=k+1
        return k==len(list1)
                
