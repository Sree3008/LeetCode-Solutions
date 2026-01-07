class Solution:
    def checkRecord(self, s: str) -> bool:
        x=s.count('A')
        print(x)
        if x>1:
            return False
        for i in range(len(s)-2):
            if s[i]==s[i+1]==s[i+2]=='L':
                return False
        return True

            
