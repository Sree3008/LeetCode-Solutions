class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s=''
        if len(word1)>len(word2):
            for i in range(len(word2)):
                s+=word1[i]
                s+=word2[i]
            else:
                for i in range(len(word2),len(word1)):
                    s+=word1[i]
        if len(word1)==len(word2):
            for i in range(len(word2)):
                s+=word1[i]
                s+=word2[i]
        if len(word2)>len(word1):
            for i in range(len(word1)):
                s+=word1[i]
                s+=word2[i]
            else:
                for i in range(len(word1),len(word2)):
                    s+=word2[i]
        return s
        

