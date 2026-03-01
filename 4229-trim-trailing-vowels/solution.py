class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        x='aeiou'
        d=''
        for i in range(len(s)-1,-1,-1):
            if s[i] in x and d=='':
                continue
            else:
                d=s[i]+d
        return d
