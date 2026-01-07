class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count = [0] * 26
        for c in word1:
            count[ord(c) - ord('a')] += 1
        for c in word2:
            count[ord(c) - ord('a')] -= 1
        
        for diff in count:
            if abs(diff) > 3:
                return False
        return True 



