class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        x=text.split()
        res=[]
        for i in range(len(x)-2):
            if x[i]==first and x[i+1]==second:
                res.append(x[i+2])
        return res 
         
