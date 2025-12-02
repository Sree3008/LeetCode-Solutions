class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l1=s1.split(' ')
        l2=s2.split(' ')
        l1=l1+l2
        l3=[]
        for i in l1:
            if l1.count(i)==1:
                l3.append(i)
        return l3


        
            
        

