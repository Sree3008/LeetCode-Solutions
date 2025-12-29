class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        x=0
        for i in s:
            if i==letter:
                x+=1
        print(x)
        y=(x*100)//len(s)
        return y
