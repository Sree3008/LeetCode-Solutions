class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        rev=s[::-1]
        flips=0
        for a,b in zip(s,rev):
            if a!=b:
                flips=flips+1
        return flips
