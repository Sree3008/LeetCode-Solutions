class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        list1=[]
        c=0
        v='aeiouAEIOU'
        for i in range(left,right+1):
            list1.append(words[i])
        for i in range(len(list1)):
            x=list1[i][0]
            y=list1[i][-1]
            if x in v and y in v:
                c+=1
        return c
