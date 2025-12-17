class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        x=Counter(arr)
        list1=[]
        for i,v in x.items():
            if v==1:
                list1.append(i)
            
        if k<=len(list1):
            y=list1[k-1]
            return y
        return ""

        
