class Solution:
    def digit_process(self,s):
        if len(s)==2:
            return s[0]==s[1]
        list1=[]
        for i in range(1,len(s)):
            x=int(s[i-1])+int(s[i])
            y=x%10
            list1.append(str(y))
        s1="".join(list1)
        return self.digit_process(s1)     
    def hasSameDigits(self, s: str) -> bool:
        return self.digit_process(s)
        

