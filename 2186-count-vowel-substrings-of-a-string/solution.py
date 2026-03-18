class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        c=0
        for i in range(len(word)):
            se=set()
            for j in range(i,len(word)):
                if word[j] not in 'aeiou':
                    break
                se.add(word[j])
                if len(se)==5:
                    c+=1
        return c
