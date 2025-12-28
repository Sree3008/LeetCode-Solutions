class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                x=words[j][::-1]
                if words[i]==words[j] or words[i]==x:
                    c+=1
        return c
