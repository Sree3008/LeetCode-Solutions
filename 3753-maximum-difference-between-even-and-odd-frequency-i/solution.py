class Solution:
    def maxDifference(self, s: str) -> int:
        x = Counter(s)
        odd = []
        even = []
        for v in x.values():
            if v % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        return max(odd) - min(even)
        
