class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low=0
        high=len(s)
        list1=[]
        for i in s:
            if i=="I":
                list1.append(low)
                low+=1
            elif i=='D':
                list1.append(high)
                high-=1
        list1.append(high)
        return list1
            

        
