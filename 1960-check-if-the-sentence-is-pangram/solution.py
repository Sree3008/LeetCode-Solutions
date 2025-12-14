class Solution:
    def checkIfPangram(self, s: str) -> bool:
        a=set(s)
        return len(a)==26

