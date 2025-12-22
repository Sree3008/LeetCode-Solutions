class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set1=set()
        set2=set()
        res=[]
        for i in range(len(A)):
            set1.add(A[i])
            set2.add(B[i])
            x=set1.intersection(set2)
            res.append(len(x))
        return res
            
            

        
