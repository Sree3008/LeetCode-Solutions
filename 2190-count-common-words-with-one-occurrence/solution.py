class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        x=Counter(words1)
        y=Counter(words2)
        list1=[]
        list2=[]
        for i,v in x.items():
            if v==1:
                list1.append(i)
        for i,v in y.items():
            if v==1:
                list2.append(i)
        c=0
        for i in list1:
            if i in list2:
                c+=1
        return c
