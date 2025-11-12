class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # while part in s:
        #     s=s.replace(part,"",1)
        # return s

        fn=lambda s:fn(s.replace(part,"",1)) if part in s else s
        return fn(s)
