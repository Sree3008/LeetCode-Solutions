class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        list1=list(s)
        # x=list(zip(indices,list1))
        x=[]
        for i,v in zip(indices,list1):
            x.append([i,v])
        x.sort()
        st=''
        for i in x:
            st+=i[1]  
        return st
        
