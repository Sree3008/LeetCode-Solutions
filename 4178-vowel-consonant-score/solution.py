class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        a='aeiou'
        v=0
        c=0
        for i in s:
            if i.isalpha():
                if i in a:
                    v+=1
                else:
                    c+=1
        if c>0:
            return floor(v/c)
        return 0
