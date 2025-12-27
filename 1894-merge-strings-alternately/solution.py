class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1=''
        list1=list(word1)
        list2=list(word2)
        if len(word1)==len(word2):
            for i in range(len(word1)):
                s1+=list1[i]
                s1+=list2[i]
        elif len(word1)>len(word2):
            for i in range(len(list1)):
                if i<len(list2):
                    s1+=list1[i]
                    s1+=list2[i]
                else:
                    s1+=list1[i]
        else:
            for i in range(len(list2)):
                if i<len(list1):
                    s1+=list1[i]
                    s1+=list2[i]
                else:
                    s1+=list2[i]
        return s1

